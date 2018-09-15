def translate(text:str) -> str:
	vowel_letters = ('a','e','i','o','u','y')
	words = text.split(' ')
	new_words = []

	for word in words:
		word = list(word)
		i = 0
		while i < len(word):
			if word[i] in vowel_letters:
				del word[i+1:i+3]
			else:
				del word[i+1]
			i += 1
		new_words.append(''.join(word))

	return ' '.join(new_words)

print(translate("hieeelalaooo")) # "hello"
print(translate("hoooowe yyyooouuu duoooiiine")) # "how you doin"
print(translate("sooooso aaaaaaaaa")) # "sos aaa"