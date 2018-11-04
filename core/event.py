from datetime import datetime

from core.keys import KeyTranslator


class Event:
	def __init__(self, key):
		self.translator = KeyTranslator()
		self.key = key
		self.time = datetime.now()

	def __str__(self) -> str:
		name = self.translator.translate(key=self.key)
		return "%s\t%s" % (name, self.time)
