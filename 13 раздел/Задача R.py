# 		Дана строка, содержащая одно или более целых чисел от $0$ до $10^9$, разделенных знаками “+” или “-”. Вычислите значение этого выражения.
# 


import re


def Eval(S):
    res = 0
    nums = re.findall(r'[+-][0-9]+', S)
    first = re.match(r'^[0-9]+', S)
    res = int(first.group(0))
    for item in nums:
        res += int(item)
    return res


print(Eval(input()))
