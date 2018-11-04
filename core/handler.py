from core.event import Event
from core.keys import KeyTranslator


class Handler:

	def __init__(self) -> None:
		self.translator = KeyTranslator

	def handle_input(self, key):
		event = Event(key, self.translator)
		formatted = str(event)
		print(formatted)
