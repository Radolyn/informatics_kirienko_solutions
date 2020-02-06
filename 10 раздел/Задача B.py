# Выведите все четные элементы списка.


inputList = list(map(int, input().split(" ")))

for i in range(0, len(inputList)):
    if inputList[i] % 2 == 0:
        print(inputList[i], end=' ')
