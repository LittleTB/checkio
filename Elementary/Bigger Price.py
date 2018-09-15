def bigger_price(limit: int, data: list) -> list:
	prices = []
	max_prices = []

	for a in data:
		prices.append(a['price'])
	prices = sorted(prices,reverse = True)

	for i in range(limit):
		for a in data:
			if prices[i] == a['price']:
				max_prices.append(a)
	return max_prices

print(bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]))