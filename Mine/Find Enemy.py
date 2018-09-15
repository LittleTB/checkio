def direction(x, n, y):
	if n == 'N':
		if (ord(y[0]) - ord(x[0])) // 2 >= abs(int(y[1]) - int(x[1])):
			return 'R'
		elif (ord(x[0]) - ord(y[0])) // 2 >= abs(int(y[1]) - int(x[1])):
			return 'L'
		elif int(y[1]) > int(x[1]):
			return 'B'
		else:
			return 'F'

print(direction("G5","N","B7"))

#def find_enemy(you, dir, enemy):





"""print(find_enemy("D3","NE","A1"))
print(find_enemy('G5', 'N', 'G4')) # == ['F', 1])
print(find_enemy('G5', 'N', 'B7')) # == ['L', 5])
print(find_enemy('G5', 'N', 'J6')) #  == ['R', 3])
print(find_enemy('A4', 'S', 'M4')) # == ['L', 12])
print(find_enemy('G3', 'NE', 'C5'))
print(find_enemy('H3', 'SW', 'E2'))
print(find_enemy("C3","SE","A1"))"""