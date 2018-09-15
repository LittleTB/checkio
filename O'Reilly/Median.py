def median(data: list) -> [int, float]:
    data = sorted(data)
    x = len(data)
    if x % 2 == 0:
        result = (data[int(x/2)] + data[int(x/2-1)]) * 0.5
    else:
        result = data[int((x-1)/2)]
    return result

print(median([3, 6, 20, 99, 10, 15]))