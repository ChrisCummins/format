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
"""This module defines a formatter for go sources."""
<<<<<<< HEAD
import os
import sys

from labm8.py import bazelutil
from tools.format import formatter
=======
from tools.format.formatters import formatter
>>>>>>> 10fbb15c0... Begin implementation of new formatter framework.


class FormatGo(formatter.Formatter):
  """Format go sources.

  Run linter on each file individually because:
    1. An error in one file prevents linting in all other files.
    2. All files in a single invocation must be in the same directory.
  """

  def __init__(self, *args, **kwargs):
<<<<<<< HEAD
    super(FormatGo, self).__init__(*args, **kwargs)
    self.gofmt = formatter.WhichOrDie("gofmt")

    # Unpack gofmt.
    arch = "mac" if sys.platform == "darwin" else "linux"
    self.gofmt = bazelutil.DataPath(f"go_{arch}/bin/gofmt")

  def RunOne(self, path):
    return formatter.ExecOrError([self.gofmt, "-w", path])
=======
    super(FormatJavaScript, self).__init__(*args, **kwargs)
    self.go = formatter.WhichOrDie("go")

  def RunOne(self, path):
    return formatter.ExecOrError([GO, "fmt", path])
>>>>>>> 10fbb15c0... Begin implementation of new formatter framework.
