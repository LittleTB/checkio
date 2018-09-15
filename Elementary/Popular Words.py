def popular_words(text: str, words: list) -> dict:
	text = text.lower().split(' ')
	count = {}

	for word in words:
		n = text.count(word) if text.count(word) else 0
		count[word] = n

	return count

print(popular_words('''When I was One I had just begun When I was Two I was nearly new''',
					['i', 'was', 'three', 'near']))
