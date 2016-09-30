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
"""This module defines a formatter for JSON files."""
from tools.format import formatter
import json

class FormatJson(formatter.Formatter):
  """Format JSON files."""

  def RunOne(self, path):
    with open(path, "r+") as f:
      data = json.load(f)
      f.seek(0)
      json.dump(data, f, indent=2, sort_keys=True)
      f.write('\n')