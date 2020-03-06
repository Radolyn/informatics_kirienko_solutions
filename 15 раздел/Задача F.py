# В выходной файл выведите все строки наибольшей длины из входного файла, не меняя их порядок.
# 

f = open('input.txt', 'r')

data = f.readlines()
ans = []

m_l = -1

for item in data:
    l = len(item)
    if l >= m_l:
        m_l = l

for item in data:
    l = len(item)
    if l == m_l:
        ans.append(item)

print(*ans, sep='')
