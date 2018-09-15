def dec_to_roman(data: int) -> str:
	"""十进制数数字转罗马数字 0 < 十进制数 < 4000"""
	digit_dict = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9}
	decade_dict = {'X':10,'XX':20,'XXX':30,'XL':40,'L':50,'LX':60,'LXX':70,'LXXX':80,'XC':90}
	hundred_dict = {'C':100,'CC':200,'CCC':300,'CD':400,'D':500,'DC':600,'DCC':700,'DCCC':800,'CM':900}
	thousand_dict = {'M':1000,'MM':2000,"MMM":3000}

	dicts = [thousand_dict,hundred_dict,decade_dict,digit_dict]
	result = ""

	# 得到各数位对应的值
	thousand = int(data / 1000) * 1000
	hundred = int((data % 1000) / 100) * 100
	decade = int((data % 100) / 10) * 10
	digit = int(data % 10)

	# 将数位值与字典中的罗马数字匹配
	for dict in dicts:
		for k,v in dict.items():
			if v == thousand:
				result += k
				break
			elif v == hundred:
				result += k
				break
			elif v == decade:
				result += k
				break
			elif v == digit:
				result += k
				break

	return result


print(dec_to_roman(3888))
print(dec_to_roman(499))
print(dec_to_roman(76))


