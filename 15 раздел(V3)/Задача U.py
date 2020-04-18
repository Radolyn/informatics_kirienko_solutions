# Известно, что фамилии всех участников — различны. Сохраните в массивах список всех участников и выведите его, отсортировав по фамилии в лексикографическом порядке. 
f = open('input.txt')
s = f.readlines()
a = []
c = 0
for i in range(len(s)):
    a.append(s[i].split())
    del a[i][2]
a = sorted(a)
for i in range(len(a)):
    print(*a[i])
