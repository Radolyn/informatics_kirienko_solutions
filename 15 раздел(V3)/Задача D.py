# Выведите все строки данного файла в обратном порядке. Для этого считайте список всех строк при помощи метода readlines().
f = open('input.txt')
s = f.readlines()
for i in range(len(s) - 1,-1,-1):
    a = s[i]
    print(a[:len(a) - 1])
f.close()
