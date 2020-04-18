# В условиях предыдущей задачи выведите фамилию и имя участника олимпиады, набравшего наибольший балл, но не ставшего победителем. Если таких школьников несколько - выведите их количество.
f = open('input.txt')
s = f.readlines()
a = []
b = []
c = 0
d = 0
for i in range(len(s)):
    for j in range(len(s[i])):
        if s[i][j].isdigit():
            a.append(s[i][j])
    b.append("".join(a))
    a = []
for i in range(len(b)):
    if b[i][0] ==  "9":
        if int(b[i][1:]) > c:
            c = int(b[i][1:])
    if b[i][:2] ==  "10" or b[i][:2] ==  "11":
        if int(b[i][2:]) > c:
            c = int(b[i][2:])
for i in range(len(b) - 1, -1, -1):
    if b[i][0] ==  "9":
        if int(b[i][1:]) == c:
            b[i] = "-1"
    elif b[i][:2] ==  "10" or b[i][:2] ==  "11":
        if int(b[i][2:]) == c:
            b[i] = "-1"
c = 0
for i in range(len(b)):
    if b[i][0] ==  "9":
        if int(b[i][1:]) > c:
            c = int(b[i][1:])
    elif b[i][:2] ==  "10" or b[i][:2] ==  "11":
        if int(b[i][2:]) > c:
            c = int(b[i][2:])
for i in range(len(b)):
    if b[i][0] ==  "9":
        if int(b[i][1:]) == c:
            d += 1
            f = i
    elif b[i][:2] ==  "10" or b[i][:2] ==  "11":
        if int(b[i][2:]) == c:    
            d += 1
            f = i
if d == 1:
    e = len(s[f]) - 1
    s[f] = list(s[f])
    while not(s[f][e].isalpha()):
        del s[f][e]
        e -= 1
    print("".join(s[f]))
else:
    print(d)
