# Дана строка. Замените в этой строке все цифры 1 на слово# one.

text = input()

text = text.replace('1', 'one')

text2 = list(text)

print("".join(text2))