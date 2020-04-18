# В условиях предыдущей задачи определите полупроходной балл, то есть такое значение балла, что количество абитуриентов, набравших балл выше полупроходного, меньше $K$, а количество абитуриентов, набравших балл выше или равный полупроходному, больше $K$.
f = open('input.txt')
s = f.readlines()
a = []
for i in range(len(s)):
    a.append(s[i].split())
    for j in range(len(a[i]) - 1, -1, -1):
        if not(a[i][j].isdigit()):
            del a[i][j]
for i in range(len(a) - 1, 0, -1):
    for j in range(len(a[i])):
        if int(a[i][j]) < 40:
            del a[i]
            break
a[0] = int("".join(a[0]))
for i in range(1, len(a)):
    a[i] = int(a[i][0]) + int(a[i][1]) + int(a[i][2])
a[1:] = sorted(a[1:], reverse = True)
b = a[0]
while a[0] + 1 < len(a) and b != 0 and a[a[0] + 1] == a[b]:
    b -= 1
if b == a[0]:
    print(0)
else:
    print(a[b + 1])
