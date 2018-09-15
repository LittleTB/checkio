def rotate(data:list, nums:list) -> list:
	dif_list = []
	count_list = []
	#q去除可以装多个炮弹的多余管号
	for num in nums:
		while nums.count(num) > 1:
			nums.remove(num)

	# 建立管道号的差值列表
	nums = sorted(nums)
	for i in range(1,len(nums)):
		dif_list.append(nums[i] - nums[0])

	# 与大炮的好坏顺序比较
	for j in range(len(data)):
		if data[j] == 1:
			for dif in dif_list:
				tmp = j + dif
				if tmp > len(data) - 1:
					tmp -= len(data)
				if data[tmp] != 1:
					break
			else:
				if nums[0] >= j:
					count_list.append(nums[0] - j)
				else:
					count_list.append(nums[0] + len(data) - j)

	return sorted(count_list)

print(rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1])) # [1, 8]
print(rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2])) # []
print(rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5])) # [0]
print(rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5])) # [0, 5]