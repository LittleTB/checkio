def convert(str_number: str, radix: int) -> int:
	"""其他进制数转十进制数"""
	nums = list(str_number)[::-1]
	result = 0

	if radix > 10:
		for i in range(len(nums)):
			if nums[i].isalpha():
				result += (ord(nums[i]) - 55) * radix ** i
			else:
				result += int(nums[i]) * radix ** i
	else:
		for i in range(len(nums)):
			result += int(nums[i]) * radix ** i

	return result


print(convert("AF", 16))
print(convert("101", 5))

