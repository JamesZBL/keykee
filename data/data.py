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
import sqlite3
from datetime import datetime

from data.repo import DBRepo


class DataRepo(DBRepo):
	_db_name = "keykee.db"
	_sql_create = '''CREATE TABLE IF NOT EXISTS 
					`KEYKEE`(`ID` INTEGER PRIMARY KEY AUTOINCREMENT , `KEY_NAME` VARCHAR ,`TIMES` INT, `DATE` DATETIME);'''
	_sql_select_all = '''SELECT * FROM `KEYKEE`;'''
	_sql_select_last_date = '''SELECT `DATE` FROM `KEYKEE` ORDER BY `ID` DESC;'''
	_sql_insert_key = '''INSERT INTO `KEYKEE` VALUES (NULL, '%s', 1, '%s');'''

	_columns = ['ID', 'KEY_NAME', 'TIMES', 'DATE']

	def __init__(self) -> None:
		connection = self._connect()
		super().__init__(self._columns, connection)
		self._init()

	def _connect(self):
		return sqlite3.connect(self._db_name, check_same_thread=False)

	def _init(self):
		self.__create__(self._sql_create)

	def _insert_key(self, keys):
		sql = ''
		for k in keys:
			sql = sql + self._sql_insert_key % (k, datetime.now())
		self.__insert__(sql)
