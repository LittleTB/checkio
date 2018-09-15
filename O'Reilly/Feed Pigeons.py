import numpy as np


def checkio(amount: int) -> int:
	nums = np.arange(1, 101).tolist()
	birds_amount = []
	sums = []

	# 生成当前时刻鸟的数量的列表
	for i in range(100):
		if i == 0:
			birds_amount.append(nums[i])
		else:
			birds_amount.append(birds_amount[i - 1] + nums[i])

	# 生成当前时刻鸟的数量共吃掉的鸟食列表
	for i in range(100):
		if i == 0:
			sums.append(birds_amount[0])
		else:
			sums.append(sums[i - 1] + birds_amount[i])

	# 将鸟食数量与鸟食列表元素比较
	for j in range(100):
		if amount == sums[j]:
			return birds_amount[j]
		elif amount >= sums[j] and amount <= sums[j + 1]:
			if (amount - sums[j]) > birds_amount[j]:
				# 判断当前剩下的鸟食够不够当前的鸟吃，只有当前的鸟食大于当前鸟的数量才有鸟食喂下一波鸟
				return amount - sums[j]
			else:
				return birds_amount[j]


print(checkio(1))
print(checkio(2))
print(checkio(3))
print(checkio(5))
print(checkio(10))
print(checkio(18))
