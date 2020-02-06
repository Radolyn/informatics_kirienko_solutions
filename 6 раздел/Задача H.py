# Дана строка, в которой буква h встречается
# как минимум два раза. Разверните последовательность символов,
# заключенную между первым и последнием появлением буквы
# h, в противоположном порядке.



text = input()


text1 = text[:text.find('h')]

text2 = text[text.find('h'):text.rfind('h') + 1]

text3 = text[text.rfind('h') + 1:]


text = text1 + text2[::-1] + text3 # reverse + add left & right positions

print(text)