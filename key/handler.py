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
from data.buffered_repo import BufferedRepo
from key.event import Event
from key.translator import KeyTranslator


class Handler:

	def __init__(self) -> None:
		self.translator = KeyTranslator()
		self.repo = BufferedRepo()

	def handle_input(self, key):
		event = Event(key, self.translator)
		formatted = str(event)
		print(formatted)
		translated = self.translator.translate(event.key)
		self.repo.insert_key(translated)
