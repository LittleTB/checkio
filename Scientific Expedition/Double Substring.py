def double_substring(line:str):
	"""取出现次数超过1的字符串的最长长度"""
	count = 0

	for i in range(len(line) - 1):
		j = i + 2
		if line.count(line[i]) > 1: # 是否出现超过1次，后面不再关心出现次数，只关心长度
			while(line.count(line[i:j]) > 1):
				j += 1
				if j > len(line):
					break
			if count < j - i - 1:
				count = j - i -1

	return count

print(double_substring('aa'))
print(double_substring('aaaa'))
print(double_substring('abc'))
print(double_substring('aghtfghkofgh'))