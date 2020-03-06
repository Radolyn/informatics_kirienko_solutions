# Известно, что фамилии всех участников — различны. Сохраните в массивах список всех участников и выведите его, отсортировав по фамилии в лексикографическом порядке.
#  

import operator

f = open('input.txt', 'r')

data = f.readlines()

people = []

for item in data:
    people.append(item.split())

people = sorted(people, key=lambda x: x[0])

for item in people:
    print(item[0], item[1], item[3])
