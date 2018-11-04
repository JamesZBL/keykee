class DBRepo:

	def __init__(self, columns) -> None:
		self._columns = columns

	def __ri__(self, column_name):
		return self._columns.index(column_name)
