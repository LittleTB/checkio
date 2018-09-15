def checkio(num:int):
	count = 0
	for i in range(32):
		if num > 2 ** i and num < 2 ** (i + 1):
			count = 1
			dif = num - 2 ** i
			while dif > 0:
				for j in range(i):
					if dif >= 2 ** j and dif < 2 ** (j + 1):
						count += 1
						dif -= 2 ** j
						break
		elif num == 2 ** i or num == 2 ** (i+1):
			count = 1

	return count

print(checkio(15))
print(checkio(14))
print(checkio(13))
print(checkio(12))