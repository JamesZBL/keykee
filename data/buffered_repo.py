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
from data.data import DataRepo


class BufferedRepo(DataRepo):
	_initial_flush_threshold = 20

	def __init__(self) -> None:
		super().__init__()
		self.key_buffer = []

	def insert_key(self, key):
		self.put_key(key)
		if len(self.key_buffer) == self._initial_flush_threshold:
			for k in self.key_buffer:
				super()._insert_key(k)
			self.key_buffer.clear()

	def put_key(self, key):
		self.key_buffer.append(key)
