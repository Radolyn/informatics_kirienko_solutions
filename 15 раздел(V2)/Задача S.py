# Задача №111344. Школы с наибольшим числом участников олимпиады
# В олимпиаде по информатике принимало участие $N$ человек. Определите
# школы, из которых в олимпиаде принимало участие больше всего участников.
# В этой задаче необходимо считывать данные построчно, не сохраняя в
# памяти данные обо всех участниках, а только подсчитывая число участников
# для каждой школы.

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

max_val = max(d1.values())

for i in d1:
    if d1[i] == max_val:  # number of max student's school
        AA.append(i)

print(*sorted(AA, key=int))
