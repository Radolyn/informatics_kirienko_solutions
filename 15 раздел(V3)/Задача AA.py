# В условиях предыдущей задачи выведите номера школ, из которых был хотя бы один участник олимпиады, в порядке убывания среднего балла участников олимпиады из этих школ. Если для двух школ средний балл участников совпадает, то их номера выводятся в порядке возрастания номера школы.
f = open('input.txt')
s = f.readlines()
a = []
b = [[0,0] for i in range(101)]
for i in range(len(s)):
    s[i] = list(s[i])
    for j in range(len(s[i])):
        if not(s[i][j].isdigit()):
            s[i][j] =  " "
    s[i] = "".join(s[i])
    a.append(s[i].split())
for i in range(len(a)):
    b[int(a[i][0])][0] += int(a[i][1])
    b[int(a[i][0])][1] += 1
    a[i] = a[i][0]
for i in range(len(b)):
    if b[i][1] != 0:
        b[i] = b[i][0] / b[i][1]
    else:
        b[i] = 0
a = sorted(a, key = int)
for i in range(len(a) - 1, 0, -1):
    if a[i] == a[i - 1]:
        del a[i]
for j in range(len(a)):
    for i in range(1, len(a)):
            if b[int(a[i])] > b[int(a[i - 1])]:
                c = a[i]
                a[i] = a[i - 1]
                a[i - 1] = c
print(*a)
