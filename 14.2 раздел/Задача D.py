# Дано число $n$. Создайте массив размером $n \times n$  и заполните его по следующему правилу. На главной диагонали должны быть записаны числа 0. На двух диагоналях, прилегающих к главной, числа 1. На следующих двух диагоналях числа 2, и т.д.




from math import *
N = int(input())
A = [[" "] * N for i in range(N)]
for i in range(N):
 for j in range(N):
   A[i][j] = abs(i-j)



for i in range(N):
 for j in range(N):
#  print(A[i][j], end = " ")
  print("{:1d}".format(A[i][j]),end = " ")
 print()

