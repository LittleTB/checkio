def check_brackets(expression):
	"""检查表达式的括号使用是否正确"""
	brackets = ''.join(a for a in expression if a in "()[]{}")

	while ("()" in brackets) or ("[]" in brackets) or ("{}" in brackets):
		brackets = brackets.replace("()","")
		brackets = brackets.replace("[]","")
		brackets = brackets.replace("{}","")

	return len(brackets) == 0



print(check_brackets("((5+3)*2+1)"))
print(check_brackets("[1+1]+(2*2)-{3/3}"))
print(check_brackets("((5+3)*2+1)+[2+2]"))
print(check_brackets("(({[(((1)-2)+3)-3]/3}-3)"))