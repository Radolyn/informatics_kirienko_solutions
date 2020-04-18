# Статья 83 закона “О выборах депутатов Государственной Думы Федерального Собрания Российской Федерации” определяет следующий алгоритм пропорционального распределения мест в парламенте. 
f = open('input.txt')
s = f.readlines()
a = []
b = 0
c = [[0,0,0]for i in range(len(s))]
d = 0
for i in range(len(s)):
    a.append(s[i].split())
    a[i].append(i)
    b += int(a[i][len(a[i]) - 2])
b /= 450
for i in range(len(a)):
    c[i][0] = int(a[i][len(a[i]) - 2]) % b
    c[i][1] = int(int(a[i][len(a[i]) - 2]) // b)
    c[i][2] = a[i][len(a[i]) - 1]
    del a[i][len(a[i]) - 1]
    d += int(c[i][1])
if d < 450:
    c = sorted(c, reverse=True)
    for i in range(len(c)):
        for j in range(len(c) - 1):
            if c[j][0] == c[j + 1][0] and c[j][1] < c[j + 1][1]:
                e = c[j]
                c[j] = c[j + 1]
                c[j + 1] = e 
    for i in range(d,450):
        c[i - d][1] += 1
    for i in range(len(c)):
        a[c[i][2]][len(a[c[i][2]]) - 1] = c[i][1]
    for i in range(len(a)):
        print(*a[i])
else:
    for i in range(len(c)):
        a[c[i][2]][len(a[c[i][2]]) - 1] = c[i][1]
    for i in range(len(a)):
        print(*a[i])    
