from collections import defaultdict


def total_cost(infos:tuple) -> int:
	cost = 0
	count = defaultdict(int)

	# 创建日期与打电话时间作为键值对的字典
	for info in infos:
		x = info[::-1].index(' ')
		mins = int(info[-x:]) // 60 if int(info[-x:]) % 60 == 0 else int(info[-x:]) // 60 + 1
		count[info[5:10]] += mins

	# 计算话费之和
	for v in count.values():
		cost += v if v <= 100 else (100 + 2 * (v - 100))

	return cost


print(total_cost(("2014-01-01 01:12:13 181",
            "2014-01-02 20:11:10 600",
            "2014-01-03 01:12:13 6009",
            "2014-01-03 12:13:55 200")))