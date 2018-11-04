from pynput.keyboard import Listener

from key.handler import Handler


class KeyListener:
	def __init__(self, handler: Handler):
		self.handler = handler

	def listen(self):
		with Listener(on_press=self.handler.handle_input) as listener:
			listener.join()
