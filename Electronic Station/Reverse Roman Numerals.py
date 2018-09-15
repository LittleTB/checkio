def roman_to_dec(data:str) -> int:
	"""罗马数字转十进制数字， 0 < 十进制数 < 4000"""
	digit_list = ['IX','VIII','VII','VI','V','IV','III','II','I']
	decade_list = ['XC','LXXX','LXX','LX','L','XL','XXX','XX','X']
	hundred_list = ['CM','DCCC','DCC','DC','D','CD','CCC','CC','C']
	thousand_list = ['MMM','MM','M']

	result = 0

	for i in range(3):
		if data.count(thousand_list[i]):
			result += 1000 * (3 - i)
			data = data.replace(thousand_list[i],'')
			break

	for j in range(9):
		if data.count(hundred_list[j]):
			if hundred_list[j] == 'D' and data.count(hundred_list[j + 1]):
				result += 100 * (8 - j)
				data = data.replace(hundred_list[j + 1], '')
			elif hundred_list[j] == 'C' and data.count('XC'):
				break
			else:
				result += 100 * (9 - j)
				data = data.replace(hundred_list[j], '')
			break

	for k in range(9):
		if data.count(decade_list[k]):
			if decade_list[k] == 'L' and data.count(decade_list[k + 1]):
				result += 10 * (8 - k)
				data = data.replace(decade_list[k + 1], '')
			elif decade_list[k] == 'X' and data.count('IX'):
				break
			else:
				result += 10 * (9 - k)
				data = data.replace(decade_list[k], '')
			break

	for m in range(9):
		if data.count(digit_list[m]):
			if digit_list[m] == 'V' and data.count(digit_list[m + 1]):
				result += (8 - m)
			else:
				result += (9 - m)
			break

	return result

print(roman_to_dec('XCIX'))
print(roman_to_dec('MMMDCCCLXXXVIII'))
print(roman_to_dec('CDXCIX'))
print(roman_to_dec('LXXVI'))


"""Perfect Solution"""
def reverse_roman(text):
	roman = ('M', 'D', 'C', 'L', 'X', 'V', 'I', '')
	arab = (1000, 500, 100, 50, 10, 5, 1)
	result = 0

	for i in range(len(text) - 1):
		now = roman.index(text[i])
		following = roman.index(text[i + 1])
		if now > following: #前一个符号对应值小于下一个符号就减，否则就加
			result -= arab[now]
		else:
			result += arab[now]

	result += arab[roman.index(text[-1])]
	return result