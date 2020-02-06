# 		Дано выражение одно из следующих видов: “A+B”, “A-B” или “A*B”, где A и B - целые числа от 0 до $10^9$. Определите значение этого выражения.
# 


def Eval(S):
    res = 0
    if S.count('+') != 0:
        a, b = S.split('+')
        res = int(a) + int(b)
    if S.count('-') != 0:
        a, b = S.split('-')
        res = int(a) - int(b)
    if S.count('*') != 0:
        a, b = S.split('*')
        res = int(a) * int(b)
    return res


print(Eval(input()))
