from key.handler import Handler
from key.listener import KeyListener


class App:
	def run(self):
		handler = Handler()
		listener = KeyListener(handler)
		listener.listen()


if __name__ == '__main__':
	app = App()
	app.run()
