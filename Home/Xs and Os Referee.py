def referee(x:list):
	#对行的判断
	for i in range(3):
		if x[i][0] != '.' and x[i].count(x[i][0]) == len(x[i]):
			return x[i][0]

	# 将列的元素放到列表
	colums = []
	for j in range(3):
		tmp1 = ''
		for k in range(3):
			tmp1 += x[k][j]
		colums.append(tmp1)

	#对列的判断
	for colum in colums:
		if colum[0] != '.' and colum.count(colum[0]) == len(colum):
			return colum[0]

	#对对角线的判断
	diagonal_left = []
	tmp_list = []
	diagonal_right = []
	for i in range(3):
		diagonal_left.append(x[i][i])
		tmp2 = x[i][::-1] #实现字符串反转
		tmp_list.append(tmp2)
	for j in range(3):
		diagonal_right.append(tmp_list[j][j])
	if diagonal_left[0] != '.' and diagonal_left.count(diagonal_left[0]) == len(diagonal_left):
		return diagonal_left[0]
	elif diagonal_right[0] != '.' and diagonal_right.count(diagonal_right[0]) == len(diagonal_right):
		return diagonal_right[0]
	else:
		return 'D'

print(referee(["X.O","XX.","XOO"]))
print(referee(["OO.","XOX","XOX"]))