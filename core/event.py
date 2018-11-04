from datetime import datetime


class Event:
	def __init__(self, key, translator):
		self.translator = translator
		self.key = str(key)
		self.time = datetime.now()

	def __str__(self) -> str:
		name = self.translator.translate(key=self.key)
		return "%s\t%s" % (name, self.time)
