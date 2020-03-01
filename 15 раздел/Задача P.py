# Зачет проводится отдельно в каждом классе. Победителями олимпиады становятся школьники, которые набрали наибольший балл среди всех участников в данном классе.
#


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
winner_of_nine, winner_of_ten, winner_of_eleven = max(
    array_of_nine), max(array_of_ten), max(array_of_eleven)
temp_1 = [array_of_nine, array_of_ten, array_of_eleven]
temp_2 = [winner_of_nine, winner_of_ten, winner_of_eleven]
for i in range(3):
    for j in range(temp_1[i].count(temp_2[i])):
        temp_1[i].remove(temp_2[i])
print(max(array_of_nine), max(array_of_ten), max(array_of_eleven))
