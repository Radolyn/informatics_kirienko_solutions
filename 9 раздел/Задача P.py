# В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.

l = list(map(int, input().split()))

max_index = l.index(max(l))
min_index = l.index(min(l))

temp_max = max(l)

l[max_index] = l[min_index]
l[min_index] = temp_max

for i in range(len(l)):
    print(l[i], end=' ')
