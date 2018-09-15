def longest_palindromic(text: str) -> str:
	max_lst = []
	count = {}

	# 建立回文字符串与其长度作为键值对的字典
	for i in range(len(text)):
		for j in range(i + 1, len(text)):
			if text[i:j + 1] == text[i:j + 1][::-1]: # 字符串两次切片
				count[text[i:j + 1]] = j - i +1

	if count:
		# 建立最长回文字符串列表
		max_value = max(list(count.values()))
		for k, v in count.items():
			if v == max_value:
				max_lst.append(k)

		if len(max_lst) > 1:
			"""选出最靠前的回文字符串"""
			# 得到最靠前字符串的列表索引，先假设第一个就是我们要找的
			left = 0
			for y in range(1, len(max_lst)):
				if text.index(max_lst[left]) > text.index(max_lst[y]):
					left = y
			return max_lst[left]
		else:
			return max_lst[0]
	else:
		return text[0]


print(longest_palindromic("artrartrt"))
print(longest_palindromic("abacada"))
