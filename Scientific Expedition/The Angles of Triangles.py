from math import pi
from math import acos


def checkio(a: int, b: int, c: int):
	x = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
	y = (a ** 2 + c ** 2 - b ** 2) / (2 * a * c)
	z = (b ** 2 + a ** 2 - c ** 2) / (2 * b * a)

	if a + b <= c or a + c <= b or b + c <= a:
		return [0, 0, 0]
	else:
		return sorted([round(acos(x) * (180 / pi)), round(acos(y) * (180 / pi)), round(acos(z) * (180 / pi))])



print(checkio(3, 4, 5))
print(checkio(2, 2, 5))
print(checkio(5, 4, 3))