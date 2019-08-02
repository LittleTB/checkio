def median(data: list) -> [int, float]:
    data = sorted(data)
    x = len(data)
    if x % 2 == 0:
        result = (data[int(x/2)] + data[int(x/2-1)]) * 0.5 # Python3中：/ 得到浮点数，// 得到的是整数（地板除）
    else:
        result = data[int((x-1)/2)]
    return result

print(median([3, 6, 20, 99, 10, 15]))