from core.data import DataRepo
from key.event import Event
from key.keys import KeyTranslator


class Handler:

	def __init__(self) -> None:
		self.translator = KeyTranslator
		self.repo = DataRepo()

	def handle_input(self, key):
		event = Event(key, self.translator)
		formatted = str(event)
		print(formatted)
