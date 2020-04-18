# В условиях предыдущей задачи выведите в порядке возрастания номера школ, в которых есть хотя бы один победитель олимпиады.
f = open('input.txt')
s = f.readlines()
a = []
b = 0
c = []
for i in range(len(s)):
    a.append(s[i].split())
for i in range(len(a)):
    if int(a[i][3]) > b:
        b = int(a[i][3])
        c = []
    if int(a[i][3]) == b:
        c.append(a[i][2])
for i in range(len(c)):
    c[i] = int(c[i])
c = sorted(c)
for i in range(len(c) - 1, 0, -1):
    if int(c[i]) == int(c[i - 1]):
        del c[i]
print(*c)
