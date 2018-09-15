def checkio(number):
    """让因数尽量大"""
    ans  = ''
    digit = 9
    while digit > 1:
        if number%digit != 0:
            digit -= 1
        else:
            ans = str(digit) + ans
            number /= digit
    if number == 1:
        return int(ans)
    else:
        return 0

print(checkio(20))
print(checkio(40))