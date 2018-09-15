def first_word(text: str) -> str:
	letters = [chr(i) for i in range(97, 123)]
	count = start = end = 0
	result = ""

	for i in range(len(text)):
		if count == 0:
			if text[i].lower() in letters:
				start = i
				count += 1

		if count == 1:
			if text[i].lower() == ',' or text[i].lower() == '.' or text[i].lower() == ' ':
				end = i
				count += 1

	if count == 1: #只有一个单词的情况
		for j in range(start,len(text)):
			result += text[j]

	elif count == 2:
		for j in range(start,end):
			result += text[j]
	return result

print(first_word("Hello world"))
print(first_word("don't touch it"))
print(first_word("hi"))