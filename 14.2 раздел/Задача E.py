# Дано число $n$. Создайте массив размером n×n и заполните его по следующему правилу:
# 



from math import *
N = int(input())
A = [[" "] * N for i in range(N)]
for i in range(N):
 for j in range(N):
   if (i + j) < (N-1):
    A[i][j] = 0
   if (i + j) == (N-1):
    A[i][j] = 1
   if (i+j) > (N-1):
    A[i][j] = 2
   

for i in range(N):
 for j in range(N):
#  print(A[i][j], end = " ")
  print("{:1d}".format(A[i][j]),end = " ")
 print()

