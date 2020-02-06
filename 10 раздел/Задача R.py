# Дан список целых чисел, число k и значение C.
# Необходимо вставить в список на позицию с индексом k элемент,
# равный C, сдвинув все элементы имевшие индекс не менее k вправо.
# 


l = list(map(int, input().split()))
nums = list(map(int, input().split()))

l.insert(nums[0], nums[1])

for i in range(len(l)):
    print(l[i], end=' ')
