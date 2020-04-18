# В выходной файл выведите все строки наибольшей длины из входного файла, не меняя их порядок.
f = open('input.txt')
s = f.readlines()
a = 0
for i in s:
    if len(i[:len(i) - 1]) > a:
        a = len(i) - 1
for i in s:
    if len(i) - 1 == a:
        print(i[:len(i) - 1])
f.close()
