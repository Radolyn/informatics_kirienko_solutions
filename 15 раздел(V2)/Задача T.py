# Задача №111345. Школы с наименьшим числом участников олимпиады
# В условиях предыдущей задачи определите школы, из которых в олимпиаде
# принимало участие меньше всего участников (но был хотя бы один
# участник).

A, AA, sortlist, d, d1 = [], [], [], {}, {}

fil = open('input.txt', 'r')

file = fil.readlines()
for item in file:
    A.append(item.split())

for item in A:
    if item[2] not in d.keys():
        d[item[2]] = 0
    d[item[2]] += int(item[3])

for item in A:
    if item[2] not in d1.keys():
        d1[item[2]] = 0
    d1[item[2]] += 1

max_val = min(d1.values())

for i in d1:
    if d1[i] == max_val:  # number of max student's school
        AA.append(i)

print(*sorted(AA, key=int))
