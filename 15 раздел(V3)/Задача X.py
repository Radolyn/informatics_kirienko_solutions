# В условиях предыдущей задачи выведите в порядке возрастания номера школ, средний балл учащихся которых выше, чем средний балл всех участников олимпиады (то есть необходимо вычислить средний балл для каждой школы и средний балл по всем участникам).
f = open('input.txt')
s = f.readlines()
a = []
b = [[0,0] for i in range(101)]
e = []
d = 0
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
    d += int(a[i][1])
for i in range(len(b)):
    if b[i][1] != 0:
        b[i] = b[i][0] / b[i][1]
    else:
        b[i] = 0
d = d / len(a)
for i in range(len(b)):
    if float(b[i]) > d:
        e.append(i)
print(*sorted(e, key = int))
