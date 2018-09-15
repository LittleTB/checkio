BRAILLE = {'a':[(1,0),(0,0),(0,0)], 'b': [(1,0),(1,0),(0,0)], 'c': [(1,1),(0,0),(0,0)],
    		 'd': [(1,1),(0,1),(0,0)], 'e': [(1,0),(0,1),(0,0)], 'f': [(1,1),(1,0),(0,0)],
			 'g': [(1,1),(1,1),(0,0)], 'h': [(1,0),(1,1),(0,0)], 'i': [(0,1),(1,0),(0.0)],
			 'j': [(0,1),(1,1),(0,0)], 'k': [(1,0),(0,0),(1,0)], 'l': [(1,0),(1,0),(1,0)],
			 'm': [(1,1),(0,0),(1,0)], 'n': [(1,1),(0,1),(1,0)], 'o': [(1,0),(0,1),(1,0)],
			 'p': [(1,1),(1,0),(1,0)], 'q': [(1,1),(1,1),(1,0)], 'r': [(1,0),(1,1),(1,0)],
			 's': [(0,1),(1,0),(1,0)], 't': [(0,1),(1,1),(1,0)], 'u': [(1,0),(0,0),(1,1)],
			 'v': [(1,0),(1,0),(1,1)], 'w': [(0,1),(1,1),(1,1)], 'x': [(1,1),(0,0),(1,1)],
			 'y': [(1,1),(0,1),(1,1)], 'z': [(1,0),(0,1),(1,1)], '0': [(0,1),(1,1),(0,0)],
			 '1': [(1,0),(0,0),(0,0)], '2': [(1,0),(1,0),(0,0)], '3': [(1,1),(0,0),(0,0)],
			 '4': [(1,1),(0,1),(0,0)], '5': [(1,0),(0,1),(0,0)], '6': [(1,1),(1,0),(0,0)],
			 '7': [(1,1),(1,1),(0,0)], '8': [(1,0),(1,1),(0,0)], '9': [(0,1),(1,0),(0.0)],
		     ' ': [(0,0),(0,0),(0,0)],'capital': [(0,0),(0,0),(0,1)],'number': [(0,1),(0,1),(1,1)],
		     "'": [(0,0),(1,0),(0,0)], '.': [(0,0),(1,1),(0,1)], '-': [(0,0),(1,1),(0,0)],
		     '?': [(0,0),(1,0),(1,1)], '_': [(0,0),(0,0),(1,1)], '!': [(0,0),(1,1),(1,0)]
			 }

def braille_page(text:str):
	chars = []
	result = []

	# 标记大写字母和数字
	for char in text:
		if char.isupper():
			chars.append('capital')
		elif char.isdigit():
			chars.append('number')
		chars.append(char)

	# 添加空格
	x = len(chars)
	if x > 10 and x % 10 != 0:
		for _ in range(10 - x % 10):
			chars.append(' ')

	# 与盲文匹配
	y = len(chars) // 10
	if x > 10:
		for _ in range(y):	# 控制行数
			for i in range(3):
				tmp = []
				for j in range(10): # 控制每行的字符数为10
					tmp.append(BRAILLE[chars[j].lower()][i][0])
					tmp.append(BRAILLE[chars[j].lower()][i][1])
					tmp.append(0)
				del tmp[-1]
				result.append(tuple(tmp))
			del chars[0:10]
			result.append(tuple([0] * 29))
		del result[-1]
	else:
		for m in range(3):
			tmp = []
			for n in range(x):
				tmp.append(BRAILLE[chars[n].lower()][m][0])
				tmp.append(BRAILLE[chars[n].lower()][m][1])
				tmp.append(0)
			del tmp[-1]
			result.append(tuple(tmp))
	return tuple(result)

print(braille_page("42"))
print(braille_page("hello 1st World!"))
#print(braille_page("Lorem Ipsum"))
