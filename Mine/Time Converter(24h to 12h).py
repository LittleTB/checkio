def time_converter(time):
	if int(time[:2]) < 12:
		if int(time[:2]) == 0:
			return '12' + time[2:5] +' a.m.'
		else:
			return str(int(time[:2])) + time[2:5] +' a.m.'
	elif int(time[:2]) == 12:
		return time + ' p.m.'
	else:
		return str(int(time[:2]) - 12) + time[2:5] +' p.m.'



print(time_converter('12:30') == '12:30 p.m.')
print(time_converter('23:15') == '11:15 p.m.')