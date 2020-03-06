

# Дан файл, каждая строка которого может содержать одно или несколько целых чисел, разделенных одним или несколькими пробелами.
#

file = open('input.txt', 'r')
b = []
debug = file.readlines()
for i in range(len(debug)):
    temp = debug[i].replace('\n', '').split()
    temp2 = 0
    for j in range(len(temp)):
        temp2 += int(temp[j])
    b.append(temp2)
for i in range(len(b)):
    print(b[i])
