

# Найдите индексы первого вхождения максимального элемента.


n, m = map(int, input().split())

d = [list(map(int, input().split())) for i in range(n)]

b = {0: 0, 1: 0}

ma = d[0][0]

for i in range(n):
    for j in range(m):
        if d[i][j] > ma:
            ma = d[i][j]
            b[0], b[1] = i, j

print(b[0], b[1])
