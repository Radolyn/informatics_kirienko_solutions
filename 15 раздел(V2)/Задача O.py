# Задача №111340. Победитель олимпиады
# Зачет в олимпиаде проводится без деления на классы. Выведите фамилию и
# имя победителя олимпиады. Если таких несколько - выведите только их
# количество.

fil = open('input.txt', 'r')
file = fil.readlines()
A, AA = [], []
for item in file:
    A.append(item.split())
max1 = -1

i = 0

for i in range(len(A)):
    if int(A[i][3]) > max1:
        max1 = int(A[i][3])
        i += 1
    else:
        i += 1

j = 0
k = 0
cheat = 0

for k in range(len(A)):
    if str(max1) in A[k]:
        cheat += 1
    else:
        k += 1

if cheat == 1:
    for j in range(len(A)):
        if str(max1) in A[j]:
            print(A[j][0], A[j][1])
        else:
            j += 1
else:
    print(cheat)

# A[i][3]
