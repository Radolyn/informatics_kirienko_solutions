# Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.


inputList = list(map(int, input().split(" ")))

for i in range(len(inputList) - 1):
    a = int(inputList[i])
    b = int(inputList[i + 1])
    if a < b:
        a = b
        print(b, end=' ')
