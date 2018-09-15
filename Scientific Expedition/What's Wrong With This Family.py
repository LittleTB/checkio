def is_family(tree):
	new_tree = [set(x) for x in tree]

	if len(tree) == 1:
		return True

	for x in tree:
		if x[::-1] in tree:
			return False

	for i in range(len(new_tree)):
		for y in new_tree[0:i] + new_tree[i+1:]:
			if new_tree[i] & y:
				break
		else:
			return False

	for j in range(len(tree)):
		for k in range(j+1,len(tree)):
			if

	return True



print(is_family([['Logan', 'Mike'],['Logan', 'Jack'],['Mike', 'Alexander']]))
print(is_family([['Logan', 'Mike'],['Logan', 'Jack'],['Mike', 'Logan']]))
print(is_family([['Logan', 'Mike'],['Logan', 'Jack'],['Mike', 'Jack']]))
print(is_family([['Logan', 'William'],['Logan', 'Jack'],['Mike', 'Alexander']]))