def between_markers(text: str, begin: str, end: str) -> str:
	result = ""
	x = len(begin)

	if begin in text and end in text:
		a = text.index(begin)
		b = text.index(end)
		if a < b:
			for i in range(a + x,b):
				result += text[i]
	elif not begin in text and end in text:
		b = text.index(end)
		for i in range(b):
			result += text[i]
	elif not end in text and begin in text:
		a = text.index(begin)
		for i in range(a + x,len(text)):
			result += text[i]
	else:
		return text
	return result

print(between_markers('No[/b] hi', '[b]', '[/b]'))
print(between_markers('No [b]hi', '[b]', '[/b]'))
print(between_markers('What is >apple<', '>', '<'))