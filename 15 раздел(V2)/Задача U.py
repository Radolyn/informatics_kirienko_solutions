# Задача №111346. Отсортировать список участников по алфавиту
# Известно, что фамилии всех участников — различны. Сохраните в массивах список всех участников и выведите его, отсортировав по фамилии в лексикографическом порядке.
# При выводе указываете фамилию, имя участника и его балл.

import operator

fil = open('input.txt', 'r')

file = fil.readlines()

people = []

for item in file:
    people.append(item.split())


def gag(x):
    return x[0]


people = sorted(people, key=gag)

for item in people:
    print(item[0], item[1], item[3])
