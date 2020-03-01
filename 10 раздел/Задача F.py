# Дан список чисел. Определите, сколько в этом списке элементов, которые
# больше двух своих соседей и выведите количество таких элементов.

inputList = list(map(int, input().split(" ")))

b = 0

for i in range(1, len(inputList) - 1):
    if int(inputList[i - 1]) < int(inputList[i]) and int(inputList[i]) > int(
            inputList[i + 1]):
        b += 1

print(b)
