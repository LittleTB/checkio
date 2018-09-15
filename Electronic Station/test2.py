text = ("abcd12345ed125ss123456789")
lst = list(text)
count = length = 0
temp = result = []

for i in range(len(lst)):
	if lst[i].isdigit():
		count += 1
		temp.append(lst[i])
		if count > length:
			length = count
			result = temp
	else:
		count = 0
		temp = []

print(''.join(result))
