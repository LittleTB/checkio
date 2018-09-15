def checkio(data:list):
	lst1 = []
	lst2 = []
	lst3 = []
	count = 0

	data = [sorted(x) for x in data]

	# 横向一跳列表
	for x in data:
		if x[0] == x[1] - 1:
			lst1.append(x)

	# 横向两跳列表
	for y in lst1:
		if [y[1],y[1] + 1] in data:
			lst2.append([y[0],y[0] + 2])

	# 横向三跳列表
	for z in lst2:
		if [z[1],z[1] + 1] in data:
			lst3.append([z[0], z[0] + 3])

	# 校验一跳列表
	for m in lst1:
		if [m[0] + 4,m[1] + 4] in lst1 and [m[0],m[0] + 4] in data and [m[1],m[1] + 4] in data:
			count += 1

	# 校验两跳列表
	for n in lst2:
		if [n[0] + 8, n[1] + 8] in lst2:
			if [n[0], n[0] + 4] in data and [n[0] + 4, n[0] + 8] in data and [n[1], n[1] + 4] in data \
				and [n[1] + 4, n[1] + 8] in data:
				count += 1
	# 校验三跳列表
	for p in lst3:
		if [p[0] + 12,p[1] + 12] in lst3:
			if [p[0],p[0]+4] in data and [p[0]+4,p[0]+8] in data and [p[0] + 8,p[0] + 12] in data \
				and [p[1], p[1] + 4] in data and [p[1] + 4, p[1] + 8] in data and [p[1] + 8, p[1] + 12] in data:
				count += 1

	return count

print(checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
     [10, 14], [12, 16], [14, 15], [15, 16]])) # 3
print(checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]])) # 2
print(checkio([[16,15],[16,12],[15,11],[11,12],[11,10],[10,14],[9,10],[14,13],[13,9],[15,14]])) # 3