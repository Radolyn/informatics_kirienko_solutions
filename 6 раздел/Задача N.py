# Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.

text = input()

text2 = ""
for i in range(0, len(text)):
    if i % 3 != 0:
        text2 += text[i]

print(text2)