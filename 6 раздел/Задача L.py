# Дана строка. Замение в этой строке все появления буквы h 
# на букву H, кроме первого и последнего вхождения.

text = input()

first = text.find('h')
second = text.rfind('h')

text = text.replace('h', 'H')

text2 = list(text)

text2[first] = text2[second] = 'h'

print("".join(text2))
