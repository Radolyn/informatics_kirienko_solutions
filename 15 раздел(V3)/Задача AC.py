# В Государственную Думу Федерального Собрания Российской Федерации выборы производятся по партийным спискам. Каждый избиратель указывает одну партию, за которую он отдает свой голос. В Государственную Думу попадают партии, которые набрали не менее 7% от числа голосов избирателей.
f = open('input.txt')
s = f.readlines()
a = []
p = 0
b = []
while s[p] != "VOTES:\n":
    a.append([s[p][:len(s[p]) - 1], 0])
    p += 1
del a[0]
for i in range(len(a) + 2,len(s)):
    for j in range(len(a)):
        if s[i] == a[j][0]:
            a[j][1] += 1
        elif s[i][:len(s[i]) - 1] == a[j][0]:
            a[j][1] += 1
for i in range(len(a)):
    a[i][1] = int(a[i][1]) / (len(s) - (2 + len(a)))
    if a[i][1] >= 0.07:  
        b.append(a[i][0])
for i in range(len(a)):
    for j in range(len(b)):
        if a[i][0] == b[j]:
            print(b[j])
