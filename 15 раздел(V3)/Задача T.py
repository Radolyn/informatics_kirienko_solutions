# В условиях предыдущей задачи определите школы, из которых в олимпиаде принимало участие меньше всего участников (но был хотя бы один участник). 
f = open('input.txt')
s = f.readlines()
a = []
b = [0] * 100

for i in range(len(s)):
    s[i] = list(s[i])
    for j in range(len(s[i])):
        if not(s[i][j].isdigit()):
            s[i][j] =  " "
    s[i] = "".join(s[i])
    a.append(s[i].split())
for i in range(len(a)):
    b[int(a[i][0])] += 1
    c = max(b)
for i in range(len(b)):
    if b[i] < c and b[i] != 0:
        c = b[i]
for i in range(len(b)):
    if int(b[i]) == c:
        print(i, end = " ")
