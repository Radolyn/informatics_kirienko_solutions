# В условиях предыдущей задачи определите школы, из которых в олимпиаде принимало участие меньше всего участников (но был хотя бы один участник). 


data = open('input.txt', 'r')

schools = {}

while data.readable():
    item = data.readline()
    item = item.split()
    if not item:
        break
    if item[2] in schools:
        schools[item[2]] += 1
    else:
        schools[item[2]] = 1

l = []
end_l = []

min_l = 200000000

for item in schools.items():
    converted = int(item[1])
    if converted < min_l:
        min_l = converted

for item in schools.items():
    if item[1] == min_l:
        end_l.append(int(item[0]))

print(*sorted(end_l))
