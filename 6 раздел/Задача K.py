# Дана строка. Удалите из этой строки все символы @.


text = input()

text = text.replace('@', '')

text2 = list(text)

print("".join(text2))
