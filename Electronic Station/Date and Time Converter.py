def date_time(date: str) -> str:
	# 日
	time = str(int(date[:2]))
	months = {
		'January':'01','February':'02','March':'03','April':'04','May':'05','June':'06',
		'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '06',
	}

	# 月
	for k,v in months.items():
		if v == date[3:5]:
			time += (' ' + k)

	# 年
	time += (' ' + date[6:10] + ' year')

	# 时
	if int(date[-5:-3]) == 1:
		time += (' 1 hour')
	else:
		time += (' ' + str(int(date[-5:-3])) + ' hours')

	# 分
	if int(date[-2:]) == 1:
		time += (' 1 minute')
	else:
		time += (' ' + str(int(date[-2:])) + ' minutes')

	return time




print(date_time("01.01.2000 00:00")) # "1 January 2000 year 0 hours 0 minutes"