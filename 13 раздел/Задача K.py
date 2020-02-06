# 		Дана строка, состоящая из n цифр (т.е. однозначных чисел), между которыми стоит $n-1$ знак операции, каждый из которых может быть либо +, либо -. Вычислите значение данного выражения.
#  


def Evaluate(S):
    res = int(S[0])
    for i in range(len(S)):
        if S[i - 1] == '+':
            res += int(S[i])
            # print('res += int(S[i])', int(S[i]))
        elif S[i - 1] == '-':
            res -= int(S[i])
            # print('res -= int(S[i])', int(S[i]))
    return res


print(Evaluate(input()))
