# Дана строка. Найдите в этой строке второе вхождение# буквы f, и выведите индекс этого вхождения. Если# буква f в данной строке встречается только один# раз, выведите число -1, а если не встречается# ни разу, выведите число -2.

text = input()

def counter(text2):
    f = 0
    for i in range(len(text2)):
        if text2[i] == "f":
            f += 1
    return f


if counter(text) == 1:
    print(-1)
elif counter(text) < 1:
    print(-2)
else:
    print(text.find('f', text.find('f') + 1))