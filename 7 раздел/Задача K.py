# Определите количество четных элементов в последовательности, завершающейся числом 0.


a = 0
b = 0

s = True

l = list()

h = 0

while s:
    n = int(input())

    if n == 0:
        print(h)
        break

    if n % 2 == 0:
        h += 1

    l.append(n)
    b += 1
