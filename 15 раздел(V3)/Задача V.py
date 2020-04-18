# Отсортируйте список участников олимпиады: 
f = open('input.txt')
s = f.readlines()
a = []
t = 0
for i in range(len(s)):
    a.append(s[i].split())
    del a[i][2]
a = sorted(a)
while t < len(a):
    for i in range(len(a) - 1):
        while int(a[i][2]) < int(a[i + 1][2]):
            b = a[i]
            a[i] = a[i + 1]
            a[i + 1] = b
    t += 1
for i in range(len(a)):
    print(*a[i])
