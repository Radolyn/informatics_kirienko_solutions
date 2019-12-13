# Найдите сумму последовательности натуральных чисел, если признаком окончания последовательности# является два подряд идущих числа 0. Числа стоящие после двух нулей в решении задачи участвовать не должны.

a = 0
b = 0

s = True

l = list()

pr = None

while s:
    n = int(input())

    if n == 0 and pr == 0:
        l.sort()
        l.reverse()
        h = 0
        m = max(l)
        for i in range(0, len(l)):
            h += l[i]
        print(h)
        break

    pr = n
    l.append(n)
    b += 1

