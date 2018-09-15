import re

def del_repeat(text:str):
	"""去除连续重复字母"""
	x = len(text)
	new_text = ""

	for i in range(x-1):
		if text[i] == text[i+1]:
			if i == x-2: #仅当比较到最后两个时才取其中一个
				new_text += text[i]
		else:
			new_text += text[i]
			if i == x-2:
				new_text += text[i+1]

	return new_text


def is_stressful(subj):
	red_words = ["help", "asap", "urgent"]
	#是否全部大写
	if subj.isupper():
		return True

	#是否以‘！！！’结尾
	elif len(subj) > 2 and subj[-1] + subj[-2] + subj[-3] == "!!!":
		return True

	#是否包含警戒词
	else:
		lower_subj = re.findall('[a-z]',subj.lower())
		new_subj = del_repeat(''.join(lower_subj))

		count = 0
		for red_word in red_words:
			if new_subj.count(red_word):
				return True
			else:
				count += 1
		if count == 3:
			return False

print(is_stressful("We need you A.S.A.P.!!"))
print(is_stressful("UUUURGGGEEEEENT here"))