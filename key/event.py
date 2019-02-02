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


class Event:

	def __init__(self, key, translator):
		self.translator = translator
		self.key = str(key)
		self.time = datetime.now()

	def __str__(self) -> str:
		name = self.translator.translate(key=self.key)
		return "%s\t%s" % (name, self.time)
