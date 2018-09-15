def to_encrypt(words,x):
	"""密码加密"""
	words = list(words)
	letters = [chr(i) for i in range(97,123)]

	for m in range(len(words)):
		if letters.count(words[m]):
			n = letters.index(words[m])
			if n+x > 25:
				words[m] = letters[n+x-26]
			else:
				words[m] = letters[n+x]
	encryped_words = ''.join(words) #以‘’内的元素将words内元素连接成字符串
	return encryped_words

print(to_encrypt("a b c", 3) )
print(to_encrypt("a b c", -3))
print(to_encrypt("simple text", 16))
print(to_encrypt("important text", 10))
print(to_encrypt("state secret", -13))