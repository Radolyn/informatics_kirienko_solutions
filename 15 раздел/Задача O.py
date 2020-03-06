# Зачет в олимпиаде проводится без деления на классы. Выведите фамилию и имя победителя олимпиады. Если таких несколько - выведите только их количество.


f = open('input.txt', 'r')

data = f.readlines()

points = []
people = []

for item in data:
    points.append(int(item.split()[3]))
    people.append(item.split())

ans = []

m_l = max(points)

i = 0
for item in points:
    if item == m_l:
        ans.append(people[i])
    i += 1

if len(ans) == 1:
    print(ans[0][0], ans[0][1])
else:
    print(len(ans))
