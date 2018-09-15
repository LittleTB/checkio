"""你将得到一个含有整数（X）的非空列表。在这个任务里，你应该返回在此列表中的非唯一元素的列表。
要做到这一点，你需要删除所有独特的元素（这是包含在一个给定的列表只有一次的元素）。
解决这个任务时，不能改变列表的顺序。例如：[1，2，3，1，3] 1和3是非唯一元素，结果将是 [1, 3, 1, 3]。"""

def select_same_factors(data:list):
    count_list = []

    for a in data:
        if data.count(a) == 1:
            count_list.append(a)

    for b in count_list:
        data.remove(b)
    return data


print(select_same_factors([1,2,3,1,3]))