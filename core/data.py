import sqlite3
from datetime import date, datetime

from core.repo import DBRepo


class DataRepo(DBRepo):

	_db_name = "keykee.db"
	_sql_create = '''CREATE TABLE IF NOT EXISTS 
					`KEYKEE`(`ID` INT PRIMARY KEY, `TIMES` INT, `DATE` DATE)'''
	_sql_select_all = '''SELECT * FROM `KEYKEE`'''
	_sql_select_last_date = '''SELECT `DATE` FROM `KEYKEE` ORDER BY `ID` DESC'''
	_sql_insert_today = '''INSERT INTO `KEYKEE` VALUES (NULL, 0, '%s')'''

	_columns = ['ID', 'TIMES', 'DATE']

	def __init__(self) -> None:
		connection = self._connect()
		super().__init__(self._columns, connection)
		self._init()

	def _connect(self):
		return sqlite3.connect(self._db_name)

	def _init(self):
		self.__create__(self._sql_create)
		last_date = self._get_last_date()
		print(last_date)
		if last_date is None:
			self._insert_today()
		elif self.__to_date__(last_date).date() < datetime.today().date():
			self._insert_today()

	def _insert_today(self):
		sql = self._sql_insert_today % date.today()
		self.__insert__(sql)

	def _get_last_date(self):
		rows = self.__select__(self._sql_select_last_date)
		if rows:
			return rows[0][0]
		return None
