# Выведите значение наименьшего нечетного элемента списка, а если в списке# нет нечетных элементов - выведите число 0.

inputList = input().split()

maxint = 2**63

a = maxint

for i in range(len(inputList)):
    b = int(inputList[i])
    if a > b and b % 2 == 1:
        a = b

if a != maxint:
    print(a)
else:
    print(0)