# В выборах Президента Российской Федерации побеждает кандидат, набравший свыше половины числа голосов избирателей. Если такого кандидата нет, то во второй тур выборов выходят два кандидата, набравших наибольшее число голосов.
f = open('input.txt')
s = f.readlines()
a = []
b = 0
c = 0
d = True
e = []
for i in range(len(s)):
    if s[i][len(s[i]) - 1] ==  "\n":
        a.append([0, s[i][:len(s[i]) - 1]])
        s[i] = s[i][:len(s[i]) - 1]
    else:
        a.append([0, s[i]])
if len(a) != 1:
    a = sorted(a)
    for i in range(len(a) - 1, -1, -1):
        if a[i][1] == a[i - 1][1]:
            del a[i]
for i in range(len(a)):
    for j in range(len(s)):
        if a[i][1] == s[j]:
            a[i][0] += 1
        if a[i][0] > b:
            c = b
            b = a[i][0]
a = sorted(a)
if a[len(a) - 1][0] > len(s) / 2:
    print(a[len(a) - 1][1])
else:
    print(a[len(a) - 1][1], a[len(a) - 2][1], sep ="\n")
