def time_converter(time):
	x = time.index(':')
	y = time.index(' ')

	if time[-4:] == 'p.m.':
		if int(time[:x]) == 12:
			new_time = time[:y]
		else:
			new_time = str(int(time[:x]) + 12) + time[x:y]
	else:
		if int(time[:x]) == 12:
			new_time = '00'+time[x:y]
		else:
			new_time = time[:y].rjust(5,'0')

	return new_time




print(time_converter('12:00 a.m.')) # '00:00'
print(time_converter('12:34 a.m.')) # '00:00'
print(time_converter('12:30 p.m.')) # '12:30'
print(time_converter('9:00 a.m.')) # '09:00'
print(time_converter('11:15 p.m.')) # '23:15'