# # 		Дана строка, возможно, содержащая пробелы. Извлеките из этой строки все символы, являющиеся цифрами и составьте из них новую строку. Решение оформите в виде функции ExtractDigits (S)#     

a = input()


def ExtractDigits(c):
    b = ''
    for i in c:
      if i.isdigit() == True:
        b += i
      else:
        pass
    return b

print(ExtractDigits(a))
