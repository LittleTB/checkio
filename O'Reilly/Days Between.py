import datetime


def days_diff(date1: tuple, date2: tuple) -> int:
	"""计算日期时间差，以天为单位"""
	d1 = datetime.datetime(date1[0],date1[1],date1[2])
	d2 = datetime.datetime(date2[0],date2[1],date2[2])

	return abs((d1 - d2).days)



print(days_diff((1982, 4, 19), (1982, 4, 22)))
print(days_diff((2014, 8, 27), (2014, 1, 1)))
