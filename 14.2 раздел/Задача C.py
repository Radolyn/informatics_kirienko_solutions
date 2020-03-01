

# Даны два числа $n$ и $m$. Создайте двумерный массив размером $n \times
# m$ и заполните его символами "." и "*" в шахматном порядке. В левом
# верхнем углу должна стоять точка.

n, m = map(int, input().split())

d = [['*' if (i + j) % 2 != 0 else '.' for i in range(m)] for j in range(n)]

for item in d:
    print(*item)
