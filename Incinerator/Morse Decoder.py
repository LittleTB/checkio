def morse_decoder(text:str):
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
	codes = text.split('   ')
	codes = [code.split(' ') for code in codes]

	word = []
	words = []

	for code in codes: # 遍历句中单词
		alphas = []
		for char in code: # 遍历单词中的字母
			for key,value in MORSE.items():
				if char == key:
					alphas.append(value)
					break
		word.append(alphas)

	word[0][0] = word[0][0].upper()

	# 将字母连成成单词
	for alphas in word:
		words.append(''.join(alphas))

	return ' '.join(words)


print(morse_decoder("... --- -- .   - . -..- -")) # "Some text"
print(morse_decoder("..--- ----- .---- ---..")) # "2018"
print(morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--")) # "It was a good day"
print(morse_decoder("----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----.   .- .-. .   -.. .. --. .. - ..."))