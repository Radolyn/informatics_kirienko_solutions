# Даны два числа $n$ и $m$. Создайте двумерный массив размером $n \times m$ и заполните его символами "." и "*" в шахматном порядке. В левом верхнем углу должна стоять точка.




from random import *
N,M = map(int,input().split())
A = [["."] * M for i in range(N)]
for i in range(N):
 for j in range(M):
  if (i + j) % 2 != 0:
   A[i][j] = "*"



for i in range(N):
 for j in range(M):
  print(A[i][j], end = " ")
#  print("{:4d}".format(A[i][j]),end = " ")
 print()

