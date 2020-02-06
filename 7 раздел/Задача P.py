# Последовательность состоит из
# натуральных чисел и завершается числом 0.
# Определите, какое количество элементов этой последовательности,
# равны ее наибольшему элементу.


a = 0
b = 0

s = True

l = list()

while s:
    n = int(input())

    if n == 0:
        l.sort()
        l.reverse()
        h = 0
        m = max(l)
        for i in range(0, len(l)):
            if m == l[i]:
                h += 1
        print(h)
        break

    l.append(n)
    b += 1
