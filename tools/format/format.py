# Copyright 2020 Chris Cummins <chrisc.101@gmail.com>.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""An opinionated, non-configurable enforcer of code style.

Usage:
  $ format <path ...>

This program enforces a consistent code style on files by modifying them in
place. If a path is a directory, all files inside it are formatted.

Features:

  * Automated code styling of C/C++, Python, Java, SQL, JavaScript, HTML,
    CSS, go, and JSON files.
  * Support for `.formatignore` files to mark files to be excluded from
    formatting. The syntax of ignore files is similar to `.gitignore`, e.g. a
    list of patterns to match, including (recursive) glob expansion, and
    patterns beginning with `!` are un-ignored.
  * Persistent caching of "last modified" timestamps for files to minimize the
    amount of work done.
  * A process lock which prevents races when multiple formatters are launched
    simultaneously.

The type of formatting applied to a file is determined by its suffix. See
format --print_suffixes for a list of suffixes which are formatted.

This program uses a filesystem cache to store various attributes such as a
database of file modified times. See `format --print_cache_path` to print the
path of the cache. Included in the cache is a file lock which prevents mulitple
instances of this program from modifying files at the same time, irrespective
of the files being formatted.
"""
import os
import pathlib
import queue
import sys
from typing import Iterable

import appdirs
import fasteners

import build_info
from labm8.py import app
from tools.format import formatter_executor
from tools.format import path_generator
from tools.format.formatters.suffix_mapping import mapping as formatters


FLAGS = app.FLAGS

app.DEFINE_boolean(
  "print_cache_path",
  False,
  "Print the path of the persistent filesystem cache and exit.",
)
app.DEFINE_boolean(
  "print_suffixes",
  False,
  "Print the list of filename suffixes which are formatted and return.",
)
app.DEFINE_boolean(
  "dry_run",
  False,
  "Only print the paths of files that will be formatted, without formatting "
  "them.",
)
app.DEFINE_boolean(
  "with_cache",
  True,
  'Enable the persistent caching of "last modified" timestamps for files. '
  "Files which have not changed since the last time the formatter was run are "
  "skipped. Running the formatter with --nowith_cache forces all files to be "
  "formatted, even if they have not changed.",
)


def GetCacheDir() -> pathlib.Path:
  """Resolve the cache directory for linters."""
  _BAZEL_TEST_TMPDIR = os.environ.get("TEST_TMPDIR")
  if _BAZEL_TEST_TMPDIR:
    os.environ["XDG_CACHE_HOME"] = _BAZEL_TEST_TMPDIR
  return pathlib.Path(
    appdirs.user_cache_dir(
      "phd_format", "Chris Cummins", version=build_info.GetBuildInfo().version
    )
  )


def Main(argv):
  if not argv:
    raise app.UsageError("Must provide a path")

  cache_dir = GetCacheDir()
  cache_dir.mkdir(parents=True, exist_ok=True)

  if FLAGS.print_cache_path:
    print(cache_dir)
    return
  elif FLAGS.print_suffixes:
    print("\n".join(sorted(formatters.keys())))
    return

  # Acquire an inter-process lock. This does not need to be released - cleanup
  # of inter-process locks using the fasteners library is automatic. This will
  # block indefinitely if the lock is already acquired by a different process,
  # ensuring that only a single formatter is running at a time.
  assert fasteners.InterProcessLock(cache_dir / "LOCK")

  paths = path_generator.PathGenerator(".formatignore").GeneratePaths(argv[1:])
  if FLAGS.dry_run:
    for path in paths:
      print(path)
  else:
    errors = FormatPaths(cache_dir, paths)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
  app.RunWithArgs(Main)
