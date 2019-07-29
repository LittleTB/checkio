def checkio(words: str) -> bool:
	"""判断字符串中是否存在三个连续英文单词"""
	words = words.split(' ')
	x = len(words)
	count = 0

	if x > 2:
		for i in range(x - 2):
			if words[i].isalpha() and words[i+1].isalpha() and words[i+2].isalpha():
				return True
			else:
				count += 1
		if count == x-2:
			return False
	else:
		return False

print(checkio("one two 3 four five six 7 eight 9 ten eleven 12"))
print(checkio("He is 123 man"))