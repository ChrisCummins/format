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
"""This module defines a formatter for JavaScript, HTML, and CSS sources."""
<<<<<<< HEAD
from labm8.py import fs
from tools.format import formatter
=======
from tools.format.formatters import formatter
>>>>>>> 10fbb15c0... Begin implementation of new formatter framework.


class FormatJavaScript(formatter.BatchedFormatter):
  """Format Javascript / HTML / CSS sources."""

  def __init__(self, *args, **kwargs):
    super(FormatJavaScript, self).__init__(*args, **kwargs)
    self.js_beautify = formatter.WhichOrDie("js-beautify")

<<<<<<< HEAD
    # Unpack the jarfile to the local cache. We do this rather than accessing
    # the data file directly since a par build embeds the data inside the
    # package. See: github.com/google/subpar/issues/43
    self.js_beautify_rc = self.cache_path / "jsbeautifyrc.json"
    if not self.js_beautify_rc.is_file():
      fs.Write(self.js_beautify_rc, '{"indent_size": 2}'.encode("utf-8"))

  def RunMany(self, paths):
    return formatter.ExecOrError(
      [self.js_beautify, "--replace", "--config", self.js_beautify_rc] + paths
=======
  def RunMany(self, paths):
    return formatter.ExecOrError(
      [self.js_beautify, "--replace", "--config", JSBEAUTIFY_RC] + paths
>>>>>>> 10fbb15c0... Begin implementation of new formatter framework.
    )
