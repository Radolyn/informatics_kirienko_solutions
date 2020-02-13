# Выведите все строки данного файла в обратном порядке. Для этого считайте список всех строк при помощи метода readlines().
# 



file = open('input.txt', 'r')
text = file.readlines()
for i in range(len(text)-1, -1, -1):
    print(text[i].replace('\n', '').replace('\\n', ''))
