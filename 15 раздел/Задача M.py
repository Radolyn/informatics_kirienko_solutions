

# В условиях предыдущей задачи определите и выведите средние баллы
# участников олимпиады в 9 классе, в 10 классе, в 11 классе.

array_of_points = [0, 0, 0]
array_of_members = [0, 0, 0]
blank_string = ''
file = open('input.txt', 'r', encoding='utf-8')
temp_array = file.readlines()
for i in range(len(temp_array)):
    last_name, first_name, class_number, points = map(
        str, temp_array[i].replace('\n', '').split())
    if int(class_number) == 9:
        array_of_points[0] += int(points)
        array_of_members[0] += 1
    elif int(class_number) == 10:
        array_of_points[1] += int(points)
        array_of_members[1] += 1
    elif int(class_number) == 11:
        array_of_points[2] += int(points)
        array_of_members[2] += 1
for i in range(3):
    try:
        blank_string += str(array_of_points[i] / array_of_members[i]) + ' '
    except BaseException:
        pass
print(blank_string)
