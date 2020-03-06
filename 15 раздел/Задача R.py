# В условиях предыдущей задачи выведите фамилию и имя участника олимпиады, набравшего наибольший балл, но не ставшего победителем. Если таких школьников несколько - выведите их количество.


f = open('input.txt', 'r')

data = f.readlines()

points = []
people = []

for item in data:
    points.append(int(item.split()[3]))
    people.append(item.split())

ans = []

m_l = max(points)

points = list(filter((m_l).__ne__, points))

m_l = max(points)

for item in people:
    if int(item[3]) == m_l:
        ans.append(item)

if len(ans) == 1:
    print(ans[0][0], ans[0][1])
else:
    print(len(ans))
