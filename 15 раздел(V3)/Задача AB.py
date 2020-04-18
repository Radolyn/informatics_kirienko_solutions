# В условиях предыдущей задачи выведите в порядке возрастания номера школ, из которых наибольшее количество участников стало победителями олимпиады.
f = open('input.txt')
s = f.readlines()
a = []
b = [0 for i in range(101)]
c = 0
d = []
for i in range(len(s)):
    s[i] = list(s[i])
    for j in range(len(s[i])):
        if not(s[i][j].isdigit()):
            s[i][j] =  " "
    s[i] = "".join(s[i])
    a.append(s[i].split())
for i in range(len(a)):
    if int(a[i][1]) > c:
        b = [0 for i in range(101)]
        c = int(a[i][1])
    if int(a[i][1]) == c:
        b[int(a[i][0])] += 1
for i in range(len(a)):
    if b[int(a[i][0])] == max(b):
        d.append(a[i][0])
d = sorted(d, key = int)
for i in range(len(d) - 2, -1, -1):
    if d[i] == d[i + 1]:
        del d[i]
print(*d)
