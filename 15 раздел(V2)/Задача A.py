# Задача №111326. A + B
# Во входном файле записано два целых числа, каждое в отдельной строке.
# Выведите в выходной файл их сумму.

# with open('ttt.txt.txt') as datfile:

#    text = datfile.read()

#print(sum(map(int, text.split())))

# with open('ttt1.txt.txt') as datfile:

#   text = datfile()

#print(sum(map(int, text.split())))

with open('input.txt') as datfile:

    text = datfile.read()

print(sum(map(int, text.split(None, 2)[:2])))
