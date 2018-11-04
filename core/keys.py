class KeyTranslator:
	def __init__(self) -> None:
		super().__init__()

	def translate(self, key):
		name = str(key)
		if name.startswith('Key.'):
			name = name.replace('Key.', '')
		if name.endswith('_r'):
			name = name.replace('_r', '')
			name = "right %s" % name

		return name
