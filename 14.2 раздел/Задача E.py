

# Дано число $n$. Создайте массив размером n×n и заполните его по следующему правилу:
#


n = int(input())

d = [[0] * (n - i - 1) + [1] + [2] * i for i in range(n)]

for item in d:
    print(*item)
