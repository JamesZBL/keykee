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
from datetime import datetime

from data.buffered_repo import buffered_repo
from key.event import Event
from key.translator import KeyTranslator


class KeyEventHandler:
	last_event_time = datetime.now()
	last_key = None
	translator = KeyTranslator()
	repo = buffered_repo
	key_space = 100 * 1000

	def handle_input(self, key):
		event = Event(key, self.translator)
		this_key = event.key
		this_time = event.time
		this_space = this_time - self.last_event_time
		if this_key != self.last_key or this_space.microseconds > self.key_space:
			translated = self.translator.translate(event.key)
			self.repo.insert_key(translated)
		self.last_event_time = this_time
		self.last_key = this_key
