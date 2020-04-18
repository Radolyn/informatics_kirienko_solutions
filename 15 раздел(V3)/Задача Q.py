# Результаты олимпиады подводятся без деления на классы. Победителем олимпиады становятся те, кто набрал больше всего баллов. Призерами олимпиады становятся участники, следующие за победителями.
f = open('input.txt')
s = f.readlines()
a = []
b = []
c = []
d = []
for i in range(len(s)):
    s[i] = list(s[i])
    for j in range(len(s[i])):
        if not(s[i][j].isdigit()):
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
e = max(max(b), max(c), max(d))
for i in range(len(b)):
    if b[i] == e:
        b[i] = -1
for i in range(len(c)):
    if c[i] == e:
        c[i] = -1
for i in range(len(d)):
    if d[i] == e:
        d[i] = -1
e = max(max(b), max(c), max(d))
f = 0
for i in range(len(b)):
    if b[i] == e:
        f += 1
for i in range(len(c)):
    if c[i] == e:
        f += 1
for i in range(len(d)):
    if d[i] == e:
        f += 1
print(e, f)
