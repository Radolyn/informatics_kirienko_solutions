# Выведите элементы данного списка в обратном порядке, не
# изменяя сам список.

inputList = input().split()

for i in reversed(inputList):
    print(i, end=' ')
