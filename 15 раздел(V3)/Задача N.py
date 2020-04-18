# В условиях предыдущей задачи определите количество школьников, ставших победителями в каждом классе. Победителями объявляются все, кто набрал наибольшее число баллов по данному классу. Гарантируется, что в каждом классе был хотя бы один участник.
f = open('input.txt')
s = f.readlines()
a = []
b = []
c = []
d = []
e = 0
f = 0
g = 0
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
for i in range(len(b)):
    if b[i] > max(b):
        e = 0
    elif int(b[i]) == max(b):
        e += 1
for i in range(len(c)):
    if c[i] > max(c):
        f = 0
    elif int(c[i]) == max(c):
        f += 1
for i in range(len(d)):
    if d[i] > max(d):
        g = 0
    elif int(d[i]) == max(d):
        g += 1
print(e, f, g)
