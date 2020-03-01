# По данным числам $n$ и $m$ заполните двумерный массив размером n×m числами от 1 до $n \times m$ “змейкой”, как показано в примере.


n, m = map(int, input().split())

d = [[j + (m * i) + 1
      for j in range(m)] if i %
     2 == 0 else list(reversed([j + (m * i) + 1
                                for j in range(m)]))
     for i in range(n)]

for item in d:
    for item2 in item:
        print("{:4d}".format(item2), end='')
    print()
