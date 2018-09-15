from datetime import date,timedelta


def weekend_counter(start, end):
	day = timedelta(days = 1)
	weekends = 0

	while start <= end:
		if start.isoweekday() > 5:
			weekends += 1
		start += day

	return weekends



print(weekend_counter(date(2013, 9, 18), date(2013, 9, 23)))
print(weekend_counter(date(2013, 1, 1), date(2013, 2, 1)))