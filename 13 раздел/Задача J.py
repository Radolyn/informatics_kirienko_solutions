# 		Дана строка, возможно, содержащая пробелы. Извлеките из этой строки все символы, являющиеся цифрами и составьте из них новую строку. Решение оформите в виде функции ExtractDigits (S)


def ExtractDigits(s):
    for c in s:
        if c.isdigit():
            yield c


res = ExtractDigits(input())

for item in res:
    print(item, end='')