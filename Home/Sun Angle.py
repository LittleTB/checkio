def sun_angle(count_time):
	"""计算太阳角度"""
	hour = int(count_time[0]+count_time[1])
	minute = int(count_time[3]+count_time[4])
	minutes = (hour - 6) * 60 + minute

	if minutes < 0 or minutes > 720:
		return "I don't see the sun!"
	else:
		angle = minutes/4
		return int(angle) if int(angle) == angle else angle

print(sun_angle("07:00"))
print(sun_angle("12:15"))
print(sun_angle("01:23"))