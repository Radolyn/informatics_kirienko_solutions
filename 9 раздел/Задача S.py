# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.
#    

l = list(map(int, input().split()))

a = 0

for item in l:
    a += l.count(item) - 1

print(a // 2)
