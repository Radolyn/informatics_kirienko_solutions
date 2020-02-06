# Определите среднее значение всех элементов последовательности, завершающейся числом 0.


a = 0
b = 0

s = True


def calc(a, b):
    print(a / b)
    exit()


while s:
    n = int(input())

    if n == 0:
        calc(a, b)

    a += n
    b += 1
