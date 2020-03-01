# Выведите подряд, без пробелов, все символы, лежащие в таблице ASCII между двумя заданными символами.


a, b = ord(input()), ord(input())

b += 1

for i in range(a, b):
    print(chr(i), end='')
