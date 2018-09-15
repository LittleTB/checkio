from collections import defaultdict


def probability(dice_number, sides, target):
	prev = {0: 1} # 表示到前一个骰子为止点数之和为几的情况有多少种
	for _ in range(dice_number): # 控制掷骰子的次数
		current = defaultdict(int) # 投当前骰子时点数之和为几的情况的种数
		for item, times in prev.items():
			for i in range(1, sides + 1): # 掷骰子
				current[item + i] += times # 与之前骰子点数之和进行相加匹配
		prev = current

	return round(current[target] / sides ** dice_number, 4)



print(probability(2,6,3))
print(probability(10, 10, 50))
print(probability(2, 3, 7))




