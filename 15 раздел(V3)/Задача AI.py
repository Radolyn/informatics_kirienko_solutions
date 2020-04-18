# В олимпиаде участвовало $N$ человек, каждый из которых мог набрать от 0 до 100 баллов. По положению об олимпиаде жюри может наградить не более 45% от числа участников, округляя их число до целого при необходимости вниз. 
f = open('input.txt')
s = f.readlines()
a = []
b = int((len(s) * 0.45) // 1) - 1
for i in range(len(s)):
    a.append(int(s[i].split()[len(s[i].split()) - 1]))
a = sorted(a, reverse = True)
if (a[b] == a[b + 1] and a[0] / 2 < a[b]) or a[b] != a[b + 1]:
    print(a[b])
else:
    while a[b] == a[b + 1]:
        b -= 1
    print(a[b])
