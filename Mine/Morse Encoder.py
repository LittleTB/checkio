def morse_encoder(text:str):
	MORSE = {'.-': 'a', '-...': 'b', '-.-.': 'c',
			 '-..': 'd', '.': 'e', '..-.': 'f',
			 '--.': 'g', '....': 'h', '..': 'i',
			 '.---': 'j', '-.-': 'k', '.-..': 'l',
			 '--': 'm', '-.': 'n', '---': 'o',
			 '.--.': 'p', '--.-': 'q', '.-.': 'r',
			 '...': 's', '-': 't', '..-': 'u',
			 '...-': 'v', '.--': 'w', '-..-': 'x',
			 '-.--': 'y', '--..': 'z', '-----': '0',
			 '.----': '1', '..---': '2', '...--': '3',
			 '....-': '4', '.....': '5', '-....': '6',
			 '--...': '7', '---..': '8', '----.': '9'
			 }
	alpha = []
	words = text.split(' ')
	for i in range(len(words)):
		words[i] = list(words[i])

	words[0][0] = words[0][0].lower()
	for word in words:
		tmp = []
		for letter in word:
			for k,v in MORSE.items():
				if letter == v:
					tmp.append(k)
		alpha.append(' '.join(tmp))

	return '   '.join(alpha)

print(morse_encoder("Some text"))
print(morse_encoder("2018"))