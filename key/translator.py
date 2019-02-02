#
# Copyright JamesZBL 2019
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class KeyTranslator:

	def __init__(self) -> None:
		super().__init__()

	def translate(self, key):
		key = self.remove_prefix(key)
		key = self.beautify_right(key)
		key = self.remove_quotation_mark(key)
		return key

	def remove_prefix(self, key):
		if key.startswith('Key.'):
			return key.replace('Key.', '')
		return key

	def beautify_right(self, key):
		if key.endswith('_r'):
			key = key.replace('_r', '')
			return "%s-right" % key
		return key

	def remove_quotation_mark(self, key):
		return key.replace('\'', '')
