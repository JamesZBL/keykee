class DBRepo:

	def __init__(self, columns, connection) -> None:
		self._columns = columns
		self.connection = connection

	def __ri__(self, column_name):
		return self._columns.index(column_name)

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
