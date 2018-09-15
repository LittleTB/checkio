from collections import defaultdict


def checkio(data:list, num:int):
	denm = len(data)
	pre = {data:1} # 到达上一次状态时的概率
	count = 0 # 最终概率

	if num != 1:
		for _ in range(num - 1):
			cur = defaultdict(int)
			for state,probability in pre.items():
				if state.count('w') == denm:
					cur[state.replace('w','b',1)] += probability
				elif state.count('b') == denm:
					cur[state.replace('b', 'w', 1)] += probability
				else:
					cur[state.replace('w','b',1)] += probability * state.count('w')/denm
					cur[state.replace('b','w',1)] += probability * state.count('b')/denm
			pre = cur

		# cur为取完倒数第二次后的状态
		for k,v in cur.items():
			count += (k.count('w')/denm * v)
	else:
		count = data.count('w')/denm

	return round(count,2)

print(checkio('bbw',3))
print(checkio('wwb',3))
print(checkio('www',3))
print(checkio('bbbb',1))
print(checkio('wwbb',4))
print(checkio('bwbwbwb',5))
