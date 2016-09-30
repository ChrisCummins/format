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
"""Unit tests for //tools/format/formatters:python."""
from labm8.py import test
from tools.format.formatters import python
from tools.format.formatters.tests import testing

FLAGS = test.FLAGS


def test_small_python_program():
  """Test pre-processing a small C++ program."""
  formatted = testing.FormatText(
      python.FormatPython,
      """
def foo():
      print('hi')
""",
  )
  print(formatted)
  assert (
    formatted
    == """\
def foo():
  print("hi")
"""
  )


if __name__ == "__main__":
  test.Main()