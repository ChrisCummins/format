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
"""This module defines a formatter for C/C++ sources."""
import sys
from labm8.py import bazelutil
from tools.format import formatter


class FormatCxx(formatter.BatchedFormatter):
  """Format C/C++ sources."""

  def __init__(self, *args, **kwargs):
    super(FormatCxx, self).__init__(*args, **kwargs)
    self.clang_format = formatter.WhichOrDie("clang-format")

    # Unpack clang-format.
    arch = "mac" if sys.platform == "darwin" else "linux"
    self.clang_format = bazelutil.DataPath(f"llvm_{arch}/bin/clang-format")


  def RunMany(self, paths):
    return formatter.ExecOrError(
      [self.clang_format, "-style", "Google", "-i"] + paths
    )