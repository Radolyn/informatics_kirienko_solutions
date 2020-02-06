# Дан список. Посчитайте, сколько в нем различных элементов, не изменяя самого списка.



l = list(map(int, input().split()))

list_ignore = list()

a = 0

for item in l:
    if list_ignore.count(item) == 0:
        a += 1
        list_ignore.append(item)

print(a)