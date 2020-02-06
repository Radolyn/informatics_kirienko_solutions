# 		Строка состоит из целых чисел, принимающих значения от $0$ до $10^9$, разделенных знаками операций “+”, “-” и “*”. Вычислите значение этого выражения выполняя действия по правилам арифметики.


import re


def Calc(S):
    nums = re.findall(r'[+-][0-9]+', S)
    first = re.match(r'^[0-9]+', S)
    res = int(first.group(0))
    for item in nums:
        res += int(item)
    return res


def Eval(S):
    repl = []
    multi = re.findall(r'[0-9]+[*][0-9]+', S)
    for item in multi:
        a, b = item.split('*')
        repl.append([item, int(a) * int(b)])
    for item in repl:
        S = S.replace(item[0], str(item[1]))
    if S.count('*') != 0:
        return Eval(S)
    return Calc(S)


print(Eval(input()))
