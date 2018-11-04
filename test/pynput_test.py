import unittest
from pynput.keyboard import Key, Listener


class TestKeyListener(unittest.TestCase):
	def on_press(self, key):
		print(key)

	def test_pynput(self):
		with Listener(on_press=self.on_press) as listener:
			listener.join()


if __name__ == '__main__':
	unittest.main()
