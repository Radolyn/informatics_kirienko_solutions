# Дано натуральное число \(N\). Определите, можно ли его представить
# в виде суммы двух точных натуральных квадратов.



n = int(input())

n = abs(n)
for i in range(int(n ** .5) + 1):
    a = (n-i**2) ** .5
    b = int(a)
    if a - b == 0:
        if i == 0 or b == 0:
            continue
        print(i, b)
        exit()

print('Impossible')
