

# Во входном файле записано два целых числа, каждое в отдельной строке.
# Выведите в выходной файл их сумму.

file = open('input.txt', 'r')
counter = 0
# print(file.readline())
for i in range(2):
    counter += int(file.readline())
print(counter)
