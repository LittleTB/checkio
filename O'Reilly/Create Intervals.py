def create_intervals(data:set) -> list:
	data = sorted(list(data))
	intervals = []

	count = 0
	if len(data) > 1:
		for i in range(len(data)-1):
			if data[i+1] - data[i] != 1:
				if i+1 == len(data) - 1:
					intervals.append((data[i-count],data[i]))
					intervals.append((data[i+1], data[i+1]))
				else:
					intervals.append((data[i-count], data[i]))
					count = 0
			else:
				if i+1 == len(data) - 1:
					intervals.append((data[i-count],data[i+1]))
				else:
					count += 1

	elif data: #只有一个元素
		intervals.append((data[0],data[0]))

	return intervals


print(create_intervals({7,9,10,11,12}))
print(create_intervals({1, 2, 3, 4, 5, 7, 8, 12}))
print(create_intervals({1, 2, 3, 6, 7, 8, 4, 5}))
print(create_intervals({}))
print(create_intervals({1}))