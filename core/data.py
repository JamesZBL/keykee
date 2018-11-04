import sqlite3
from datetime import date

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
		super().__init__(self._columns)
		self._connect()
		self._init()
		self.connection = None

	def _connect(self):
		self.connection = sqlite3.connect(self._db_name)

	def _init(self):
		c = self._get_cursor()
		c.execute(self._sql_create)
		self._commit()
		last_date = self._get_last_date()
		if last_date is None:
			self._insert_today()

	def _insert_today(self):
		sql = self._sql_insert_today % date.today()
		c = self._get_cursor()
		c.execute(sql)
		self._commit()

	def _get_last_date(self):
		c = self._get_cursor()
		c.execute(self._sql_select_last_date)
		return None

	def _get_cursor(self):
		return self.connection.cursor()

	def _commit(self):
		self.connection.commit()
