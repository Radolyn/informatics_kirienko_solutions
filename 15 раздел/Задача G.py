# Определите, есть ли во входном файле символ '@'. Выведите слово YES или NO.
#


def check(array):
    for i in range(len(array)):
        if '@' in array[i]:
            return 'YES'
    return 'NO'


file = open('input.txt', 'r')
debug = file.readlines()
print(check(debug))
