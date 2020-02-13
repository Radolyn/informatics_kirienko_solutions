# Найдите индексы первого вхождения максимального элемента.




from random import *
x = 0
y = 0
N,M = map(int,input().split())
A = [[0] * M for i in range(N)]
for i in range(N):
 B = input().split()
 for j in range(M):
  A[i][j] = int(B[j])
ch = A[0][0]
for i in range(N):
 for j in range(M):
  if A[i][j] > ch:
   ch = A[i][j]
   x = i
   y = j
print(x,y)
#  print("{:4d}".format(A[i][j]),end = " ")
# print()

