# Дан список, упорядоченный по неубыванию элементов в нем.# Определите, сколько в нем различных элементов.

inputList = input().split()

b = 0

for i in range(0, len(inputList) - 1 ):
    if int(inputList[i]) != int(inputList[i + 1]):
        b += 1

print(b + 1)