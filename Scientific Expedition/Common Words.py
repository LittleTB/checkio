def checkio(first, second):
	lst1 = first.split(',')
	lst2 = second.split(',')

	common_words = []
	for word in lst1:
		if word in lst2:
			common_words.append(word)

	return ','.join(sorted(common_words))




print(checkio("hello,world", "hello,earth"))
print(checkio("one,two,three", "four,five,six"))
print(checkio("one,two,three", "four,five,one,two,six,three"))