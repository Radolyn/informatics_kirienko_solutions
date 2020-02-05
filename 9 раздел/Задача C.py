# Найдите количество положительных элементов в данном списке.

inputList = list(map(int, input().split(" ")))

b = 0

for i in inputList:
  if i > 0:
    b += 1
print(b)