# Результаты олимпиады подводятся без деления на классы. Победителем олимпиады становятся те, кто набрал больше всего баллов. Призерами олимпиады становятся участники, следующие за победителями.
# 



import collections
array_of_points = []
file = open('input.txt', 'r', encoding='utf-8')
array_of_lines = file.readlines()
for i in range(len(array_of_lines)):
    last_name, first_name, class_number, points = map(
        str, array_of_lines[i].replace('\n', '').split())
    array_of_points.append(int(points))
temp_max = max(array_of_points)
for i in range(array_of_points.count(temp_max)):
    array_of_points.remove(temp_max)
print(max(array_of_points), array_of_points.count(max(array_of_points)))