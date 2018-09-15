"""如果密码的长度大于或等于10个字符，且其中至少有一个数字、一个大写字母和一个小写字母，该密码将被视为足够强大。密码只包含ASCII拉丁字母或数字。
输入: 密码。
输出: 密码的安全与否，作为布尔值(bool)，或者任何可以转换和处理为布尔值的数据类型。你会在结果看到转换后的结果(True 或 False)。"""

import re


def check_password(data:str) ->bool:
    if not len(data) >=10:
        return False
    elif not re.search('[a-z]',data):
        return False
    elif not re.search('[A-Z]',data):
        return False
    elif not re.search('[0-9]',data):
        return False
    return True

print(check_password('A1213pokl'))
print(check_password('bAse730onE'))
