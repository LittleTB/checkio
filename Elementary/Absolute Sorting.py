def checkio(numbers_array: tuple) -> list:
	"""将元组按绝对值大小排序"""
	nums = list(numbers_array)
	# sort()函数法
	#nums.sort(key=abs)
	# 冒泡法
	tmp = 0
	for i in range(len(nums)):
		flag = False
		for j in range(len(nums)-i-1):
			if abs(nums[j]) > abs(nums[j+1]):
				tmp = nums[j]
				nums[j] = nums[j+1]
				nums[j+1] = tmp
				flag = True
		if not flag:
			braak

	return tuple(nums)

print(checkio((-20, -5, 10, 15)))