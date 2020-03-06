

# В олимпиаде по информатике принимало участие несколько человек.
# Победителем олимпиады становится человек, набравший больше всех баллов.
# Победители определяются независимо по каждому классу. Определите
# количество баллов, которое набрал победитель в каждом классе.
# Гарантируется, что в каждом классе был хотя бы один участник.

array = [0, 0, 0]
file = open('input.txt', 'r', encoding='utf-8')
temp_array = file.readlines()
for i in range(len(temp_array)):
    last_name, first_name, class_number, points = map(
        str, temp_array[i].replace('\n', '').split())
    if class_number == '9' and int(points) >= array[0]:
        array[0] = int(points)
    elif class_number == '10' and int(points) >= array[1]:
        array[1] = int(points)
    elif class_number == '11' and int(points) >= array[2]:
        array[2] = int(points)
print(*array)
