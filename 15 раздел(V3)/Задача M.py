# В условиях предыдущей задачи определите и выведите средние баллы участников олимпиады в 9 классе, в 10 классе, в 11 классе.
f = open('input.txt')
s = f.readlines()
a = []
b = []
c = [0,0]
d = [0,0]
e = [0,0]
for i in range(len(s)):
    for j in range(len(s[i])):
        if s[i][j].isdigit():
            a.append(s[i][j])
    b.append("".join(a))
    a = []
for i in range(len(b)):
    if b[i][0] ==  "9":
        d[0] += int(b[i][1:])
        d[1] += 1
    if b[i][:2] ==  "10":
        c[0] += int(b[i][2:])
        c[1] += 1
    if b[i][:2] ==  "11":
        e[0] += int(b[i][2:])
        e[1] += 1
print(d[0] / d[1], c[0] / c[1], e[0] / e[1])
