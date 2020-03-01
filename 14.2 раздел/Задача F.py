

# Дан двумерный массив и два числа: $i$ и $j$. Поменяйте в массиве столбцы
# с номерами $i$ и $j$


def SwapColumns(d, i, j):
    for column in d:
        column[i], column[j] = column[j], column[i]
    return d


n, m = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(n)]
i, j = map(int, input().split())

swaped = SwapColumns(d, i, j)

for item in swaped:
    print(*item)
