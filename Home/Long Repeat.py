"""找到字符串中最长的相同字符重复出现的次数，并返回它的重复次数。
例如：字符串“aaabbcaaaa”包含具有相同字母“aaa”，“bb”，“c”和“aaaa”的四个子字符串。
最后一个子字符串是最长的一个字符串，你应该返回 4 。"""

def long_repeat(line):
    count =0
    for char in line:
        newchar = char
        while(line.count(newchar)>0):
            newchar += char
        if count < len(newchar)-1:
            count = len(newchar)-1
    print(count)

long_repeat('sdsffffse')
long_repeat('ddvvrwwwrggg')