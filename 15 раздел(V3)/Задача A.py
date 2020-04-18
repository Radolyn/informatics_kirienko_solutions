# Во входном файле записано два целых числа, каждое в отдельной строке. Выведите в выходной файл их сумму.
f = open('input.txt')
s = f.readlines()
a = 0
for i in s:
    a += int(i)
print(a)
f.close()
