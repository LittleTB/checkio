from collections import defaultdict

def fastest_horse(races:list):
	count = defaultdict(int)

	for race in races:
		for i in range(len(race)):
			race[i] = 60 * int(race[i][0]) + int(race[i][2:4])

	for race in races:
		for j in range(len(race)):
			if race[j] == min(race):
				count[j + 1] += 1

	for k,v in count.items():
		if v == max(count.values()):
			return k

print(fastest_horse([["1:13", "1:26", "1:11"], ["1:10", "1:18", "1:14"], ["1:20", "1:23", "1:15"]])) # 3