def baseThree(num, numerals="012"):
    return ((num == 0) and numerals[0]) or (baseThree(num // 3, numerals).lstrip(numerals[0]) + numerals[num % 3])
num=int(input())
print(baseThree(num))

