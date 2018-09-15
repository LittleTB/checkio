def non_repeat(line):
	x = len(line)
	count = 0
	flag = True
	result = new_line = ""

	for i in range(x):
		if not line[i] in new_line:
			if i == x-1:
				#最后一个字母不在当前字符串中时，需要比较这条字符串长度与之前最长不重复的长度以决定输出的字符串
				if len(new_line) + 1 > count:
					result = new_line + line[i]
			else:
				new_line += line[i]

		else:
			if count < len(new_line):
				count = len(new_line)
				result = new_line

			#新的不重复字符串
			y = new_line.index(line[i])
			tmp_line = ""
			for j in range(y+1,len(new_line)):
				tmp_line += new_line[j]
			new_line = tmp_line + line[i]

			flag = False
	if flag:
		result = line

	return result

print(non_repeat('abcabcffab'))
print(non_repeat('a'))
print(non_repeat('abcd'))
print(non_repeat("fghfrtyfgh"))
print(non_repeat("abcdcef"))