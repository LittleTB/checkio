def repeat_inside(line:str):
	count = {}

	# 建立重复字符串与重复次数作为键值对的字典
	for i in range(len(line)):
		if line.count(line[i]) > 1:
			for j in range(i+1,len(line)):
				if line[i] == line[j]:
					char = line[i:j]
					k = 0 #字符串重复次数
					while(line.count(char) > 0):
						char += line[i:j]
						k += 1
					if k > 1:
						x = len(char)
						y = j - i
						count[char[:x-y]] = k
					break

	if count:
		# 建立重复次数最大字符串的列表
		max_value = max(list(count.values()))
		max_lst = []
		for k,v in count.items():
			if v == max_value:
				max_lst.append(k)

		# 选出重复次数最大字符串中最长的字符串
		if len(max_lst) > 1:
			longest = 0
			for z in range(1,len(max_lst)):
				if len(max_lst[longest]) < len((max_lst[z])):
					longest = z
			return max_lst[longest]
		else:
			return max_lst[0]
	else:
		return ''



print(repeat_inside('abcabcabab'))
print(repeat_inside('aaaa'))
print(repeat_inside('aabbff'))
print(repeat_inside('aababff'))
print(repeat_inside('abc'))