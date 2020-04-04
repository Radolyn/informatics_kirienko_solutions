# Задача №111348. Школы, в которых есть победители олимпиады
# В условиях предыдущей задачи выведите в порядке возрастания номера школ,
# в которых есть хотя бы один победитель олимпиады.

fil = open('input.txt', 'r')

file = fil.readlines()

array_of_school = [0] * 100

max1 = 0

for item in file:
    last_name, first_name, school_number, points = map(
        str,
        item.replace('\n', '').split())
    if max1 <= int(points):
        max1 = int(points)

for item in file:
    last_name, first_name, school_number, points = map(
        str,
        item.replace('\n', '').split())
    if int(points) == max1:
        array_of_school[int(school_number)] += 1

for i in range(1, 100):
    if array_of_school[i] != 0:
        print(i, end=' ')

fil.close()
