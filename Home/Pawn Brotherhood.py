def safe_pawns(coordinates : set):
	"""判定棋子是否安全只需判断其左下与右下是否有棋子"""
	colums = "abcdefgh"
	nums = 0
	for coordinate in coordinates:
		lst = list(coordinate)
		x = colums.index(lst[0])
		if lst[1] != '1': #第1行的棋子都不安全
			if x == 0: #第1列不存在左下
				bottom_right = colums[x+1] + str(( int(lst[1]) - 1 ))
				if bottom_right in coordinates:
					nums += 1
			elif x == 7: #第8列不存在右下
				bottom_left = colums[x - 1] + str((int(lst[1]) - 1))
				if bottom_left in coordinates :
					nums += 1
			else:
				bottom_right = colums[x + 1] + str((int(lst[1]) - 1))
				bottom_left = colums[x - 1] + str((int(lst[1]) - 1))
				if bottom_left in coordinates or bottom_right in coordinates:
					nums += 1
	return nums

print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))
print(safe_pawns({"a8", "b7", "c6", "d5", "e4", "f3", "g2","h1"}))