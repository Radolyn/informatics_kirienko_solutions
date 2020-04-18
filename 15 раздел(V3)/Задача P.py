# Зачет проводится отдельно в каждом классе. Победителями олимпиады становятся школьники, которые набрали наибольший балл среди всех участников в данном классе.
f = open('input.txt')
s = f.readlines()
a = []
b = []
c = []
d = []
for i in range(len(s)):
    s[i] = list(s[i])
    for j in range(len(s[i])):
        if s[i][j].isalpha():
            s[i][j] =  " "
    s[i] = "".join(s[i])
    a.append(s[i].split())
for i in range(len(a)):
    if a[i][0] ==  "9":
        b.append(int(a[i][1]))
    if a[i][0] ==  "10":
        c.append(int(a[i][1]))
    if a[i][0] ==  "11":
        d.append(int(a[i][1]))
e = max(b)
f = max(c)
g = max(d)
for i in range(len(b) - 1, -1, -1):
    if b[i] == e:
        del b[i]
for i in range(len(c) - 1, -1, -1):
    if c[i] == f:
        del c[i]
for i in range(len(d) - 1, -1, -1):
    if d[i] == g:
        del d[i]
print(max(b), max(c), max(d))
