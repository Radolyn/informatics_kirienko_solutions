# Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа.
# Если соседних элементов одного знака нет - не выводите ничего. Если таких пар соседей
# несколько - выведите первую пару.


inputList = list(map(int, input().split(" ")))

for i in range(len(inputList) - 1):
    a = int(inputList[i])
    b = int(inputList[i + 1])
    if 0 < (a * b):
        print(a, b, end=' ')
        break
