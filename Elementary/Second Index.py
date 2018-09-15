def second_index(text: str, symbol: str) -> [int, None]:
	lst = list(text)

	if text.count(symbol) > 1:
		lst.remove(symbol)
		return lst.index(symbol) + 1

print(second_index("sims", "s"))