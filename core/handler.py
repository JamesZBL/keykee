from core.event import Event


class Handler:
	def handle_input(self, key):
		event = Event(key)
		formatted = str(event)
		print(formatted)
