

# В файле могут быть записаны десятичные цифры и все, что угодно. Числом назовем последовательность цифр, идущих подряд (т.е. число всегда неотрицательно).
#

import re
counter = 0
# try:
file = open('input.txt', 'r')
temp = re.findall(r"[0-9]+", ' '.join(file.readlines()))
for i in range(len(temp)):
    counter += int(temp[i])
print(counter)
# except:
#   print(counter)6
