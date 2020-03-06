# В олимпиаде по информатике принимало участие $N$ человек. Определите школы, из которых в олимпиаде принимало участие больше всего участников. В этой задаче необходимо считывать данные построчно, не сохраняя в памяти данные обо всех участниках, а только подсчитывая число участников для каждой школы.


import operator

f = open('input.txt', 'r')

data = f.readlines()

people = []

for item in data:
    people.append(item.split())

schools = {}

for item in people:
    n = int(item[2])
    if n not in schools:
        schools[n] = 0
    else:
        schools[n] += 1

m_l = max(schools.items(), key=operator.itemgetter(1))[1]
schools2 = sorted(schools)

for item in schools2:
    if schools[item] == m_l:
        print(item, end=' ')
