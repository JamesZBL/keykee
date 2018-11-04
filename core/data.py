import sqlite3

from core.repo import DBRepo


class DataRepo(DBRepo):
	_db_name = "keykee.db"
	_sql_create = '''CREATE TABLE IF NOT EXISTS 
					`KEYKEE`(`ID` INTEGER PRIMARY KEY, `TIMES` INT(8), `DATE` DATE)'''
	_sql_select = '''SELECT * FROM `KEYKEE`'''
	_columns = ['ID', 'TIMES', 'DATE']

	def __init__(self) -> None:
		super().__init__(self._columns)
		self._connect()
		self._init()
		self.connection = None
		self.cursor = None

	def _connect(self):
		self.connection = sqlite3.connect(self._db_name)
		self.cursor = self.connection.cursor()

	def _init(self):
		self.cursor.execute(self._sql_create)
