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


class DBRepo:

	def __init__(self, columns, connection) -> None:
		self._columns = columns
		self.connection = connection

	def __ri__(self, column_name):
		return self._columns.index(column_name)

	def __to_date__(self, raw_date):
		return datetime.strptime(raw_date, '%Y-%m-%d')

	def __select__(self, sql):
		cn = self.connection
		c = cn.cursor()
		c.execute(sql)
		row_set = []
		for row in c:
			row_set.append(row)
		return row_set

	def __create__(self, sql):
		cn = self.connection
		c = cn.cursor()
		c.execute(sql)
		cn.commit()

	def __update__(self, sql):
		cn = self.connection
		c = cn.cursor()
		c.execute(sql)
		cn.commit()

	def __insert__(self, sql):
		cn = self.connection
		c = cn.cursor()
		c.execute(sql)
		cn.commit()

	def __deletee__(self, sql):
		cn = self.connection
		c = cn.cursor()
		c.execute(sql)
		cn.commit()
