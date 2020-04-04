# Задача №111331. Длинные строки
# В выходной файл выведите все строки наибольшей длины из входного файла, не меняя их порядок.
# В данной задаче удобно считать список строк входного файла целиком при
# помощи метода readlines().

fil = open('input.txt', 'r')
file = fil.readlines()
i = 0
AA = []
fuck = -1

for item in file:
    gg = len(item)
    if gg >= fuck:
        fuck = gg

for item in file:
    gg = len(item)
    if gg == fuck:
        AA.append(item)

print(*AA, sep='')
