# В условиях предыдущей задачи определите количество школьников, ставших
# победителями в каждом классе. Победителями объявляются все, кто набрал
# наибольшее число баллов по данному классу. Гарантируется, что в каждом
# классе был хотя бы один участник.


array_of_nine, array_of_ten, array_of_eleven = [], [], []
file = open('input.txt', 'r', encoding='utf-8')
array_of_lines = file.readlines()
for i in range(len(array_of_lines)):
    last_name, first_name, class_number, points = map(
        str, array_of_lines[i].replace('\n', '').split())
    if class_number == '9':
        array_of_nine.append(int(points))
    elif class_number == '10':
        array_of_ten.append(int(points))
    elif class_number == '11':
        array_of_eleven.append(int(points))
print(array_of_nine.count(max(array_of_nine)), array_of_ten.count(
    max(array_of_ten)), array_of_eleven.count(max(array_of_eleven)))
