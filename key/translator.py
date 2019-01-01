class KeyTranslator:

	def __init__(self) -> None:
		super().__init__()

	def translate(self, key):
		key = self.remove_prefix(key)
		key = self.beautify_right(key)
		key = self.remove_quotation_mark(key)
		return key

	def remove_prefix(self, key):
		if key.startswith('Key.'):
			return key.replace('Key.', '')
		return key

	def beautify_right(self, key):
		if key.endswith('_r'):
			key = key.replace('_r', '')
			return "%s-right" % key
		return key

	def remove_quotation_mark(self, key):
		return key.replace('\'', '')
