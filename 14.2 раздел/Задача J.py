# Дан двумерный массив размером n×n. Транспонируйте его и результат запишите в этот же массив. Вспомогательный массив использовать нельзя. Решение оформите в виде функции Transpose (A).


n = int(input())

d = [list(map(int, input().split())) for j in range(n)]

for i in range(n):
    for j in range(n):
        if j > i:
            d[i][j], d[j][i] = d[j][i], d[i][j]

for item in d:
    print(*item)
