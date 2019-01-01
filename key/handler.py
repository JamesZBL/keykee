from data.buffered_repo import BufferedRepo
from key.event import Event
from key.translator import KeyTranslator


class Handler:

	def __init__(self) -> None:
		self.translator = KeyTranslator()
		self.repo = BufferedRepo()

	def handle_input(self, key):
		event = Event(key, self.translator)
		formatted = str(event)
		print(formatted)
		translated = self.translator.translate(event.key)
		self.repo.insert_key(translated)
