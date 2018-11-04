class KeyTranslator:
	def __init__(self) -> None:
		super().__init__()

	def translate(self, key):
		key = self.remove_prefix(key)
		key = self.beautify_right(key)
		return key

	def remove_prefix(self, key):
		if key.startswith('Key.'):
			return key.replace('Key.', '')
		return key

	def beautify_right(self, key):
		if key.endswith('_r'):
			key = key.replace('_r', '')
			return "right %s" % key
		return key