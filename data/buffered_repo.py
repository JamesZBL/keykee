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
import datetime

from data.data import DataRepo


class BufferedRepo(DataRepo):
	_initial_flush_threshold = 20
	key_buffer = []

	def __init__(self) -> None:
		super().__init__()

	def insert_key(self, key):
		self.put_key(key)
		if len(self.key_buffer) == self._initial_flush_threshold:
			super()._insert_key(self.key_buffer)
			self.key_buffer.clear()

	def put_key(self, key):
		self.key_buffer.append(key)

	def find_keys(self):
		key_tuples = super().__select__(self._sql_select_keys)
		keys = []
		i = 1
		for k in key_tuples:
			tmp = {'order': i, 'name': k[0], 'count': k[1]}
			keys.append(tmp)
			i = i + 1
		return keys

	def find_total_count(self):
		total_tuples = super().__select__(self._sql_select_total_count)
		return total_tuples[0][0]

	def find_recent(self, count=10):
		_sql = self._sql_select_recent.format(count)
		recent_tuples = super().__select__(_sql)
		recent = []
		for c in recent_tuples:
			tmp = {'count': c[0], "date": c[1]}
			recent.append(tmp)
		return recent

	def find_today_count(self):
		str_date = datetime.datetime.now().strftime('%Y-%m-%d')
		count_tuple = super().__select__(self._sql_select_total_today.format(str_date))
		return count_tuple[0][0]

	def find_whole_day(self):
		count_tuples = super().__select__(self._sql_select_keys_whole_day)
		whole_day_dict = {}
		for i in count_tuples:
			hour_str = i[0]
			count = i[1]
			hour = int(hour_str)
			whole_day_dict[hour] = count
		whole_day = []
		for i in range(0, 24):
			try:
				count = whole_day_dict[i]
				whole_day.append({'hour': i, 'count': count})
			except KeyError:
				whole_day.append({'hour': i, 'count': 0})
		return whole_day


buffered_repo = BufferedRepo()
