# Формат входных данных аналогичен предыдущей задаче. Выведите список всех партий, участвовавших в выборах, отсортировав его в порядке убывания количества голосов избирателей, а при равном количестве голосов - в лексикографическом порядке.
f = open('input.txt')
s = f.readlines()
a = []
p = 1
b = []
while s[p] != "VOTES:\n":
    a.append([s[p][:len(s[p]) - 1], 0])
    p += 1
for i in range(len(a) + 2,len(s)):
    for j in range(len(a)):
        if s[i] == a[j][0]:
            a[j][1] += 1
        elif s[i][:len(s[i]) - 1] == a[j][0]:
            a[j][1] += 1
a = sorted(a)
for i in range(len(a)):
    for i in range(1, len(a)):
        if a[i][1] > a[i - 1][1]:
            g = a[i]
            a[i] = a[i - 1]
            a[i - 1] = g
for i in range(len(a)):
    print(a[i][0])
