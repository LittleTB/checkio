def all_the_same(lst):
	"""判定列表元素是否全部相同"""
	return False if lst and lst.count(lst[0]) != len(lst) else True


print(all_the_same([1,1,3]))
print(all_the_same([1,2,3,1]))
print(all_the_same([1,1,1,1]))
print(all_the_same([]))
print(all_the_same([1]))
