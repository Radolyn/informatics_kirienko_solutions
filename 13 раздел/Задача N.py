# Дана строка, возможно, содержащая пробелы. Определите количество слов в этой строке. Слово — это несколько подряд идущих букв латинского алфавита (как заглавных, так и строчных).
# 

import re as regular_ex


def removeTrash(s):
    l1 = s.count('-')
    for i in range(l1):
        del s[s.index('-')]
    return s


s = input()

r = r"[A-Za-z]+"

t = removeTrash(regular_ex.findall(r, s))

l = len(t)

print(l)
