"""给你一段文本，其中包含不同的英文字母和标点符号。
你要找到其中那个出现最多的 字母，返回的字母必须是 小写形式。
找这个“头号通缉字母”时，大小写不重要，所以对于你的搜索而言 "A" == "a"。 注意不要管标点符号、数字和空格，我们只要字母！
如果你找到 两个或两个以上出现频率相同的字母， 那么返回字母表中靠前的那个。 """

import re
from collections import Counter


def get_max_value(text):
    text = text.lower()
    result = re.findall('[a-zA-Z]', text)
    count = Counter(result) # 生成一个元素-数量为键值对的字典

    count_list = list(count.values())
    max_value = max(count_list)
    max_list = []

    for k, v in count.items():
        if v == max_value:
            max_list.append(k)
    max_list = sorted(max_list)

    print(max_list[0])


while True:
    a = input("输入一个字符串：")
    get_max_value(a)