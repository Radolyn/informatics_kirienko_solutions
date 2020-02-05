# 
# 	Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного.
#     

n = int(input())
if n >= 11 and n <= 14:
    print(n, 'korov')
else:
    temp = n % 10
    if temp == 0 or (temp >= 5 and temp <= 9):
        print(n, 'korov')
    if temp == 1:
        print(n, 'korova')
    if temp >= 2 and temp <= 4:
        print(n, 'korovy')
