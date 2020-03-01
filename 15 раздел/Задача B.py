# Во входном файле записано два целых числа, которые могут быть разделены пробелами и концами строк. Выведите в выходной файл их сумму.
#


import re
file = open('input.txt', 'r')
counter = 0
temp = re.findall(r"[0-9/-]+", ' '.join(file.read().split()))
for i in range(len(temp)):
    counter += int(temp[i])
print(counter)
