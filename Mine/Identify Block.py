def identify_block(nums:set) -> str:
	nums = sorted(list(nums))
	new_nums = ''.join(nums)
	rows = ['1234','5678','9101112','13141516']
	colums = ['15913','261014','371115','481216']

	if new_nums in rows or new_nums in colums:
		return 'I'



print(identify_block({1, 2, 3, 4}) == 'I')
print(identify_block({1, 2, 3, 6}) == 'T')
print(identify_block({1, 5, 6, 10}) == 'S')