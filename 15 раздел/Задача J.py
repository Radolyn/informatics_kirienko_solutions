# Дан файл. Определите сколько в нем букв (латинского алфавита), слов, строк. Выведите три найденных числа в формате, приведенном в примере.
# 

import re

f = open('input.txt', 'r')


def removeTrash(s):
    l1 = s.count('-')
    for i in range(l1):
        del s[s.index('-')]
    return s


def count_words(s):
    r = r"[A-Za-z]+"

    t = removeTrash(re.findall(r, s))

    return len(t)


def count_letters(s):
    r = r"[A-Za-z]+"
    t = removeTrash(re.findall(r, s))
    l = 0
    for item in t:
        l += len(item)
    return l


data = f.readlines()
ans = {'letters': 0, 'words': 0, 'lines': 0}

ans['lines'] = len(data)

for item in data:
    item = item[:-1]
    ans['words'] += count_words(item)
    ans['letters'] += count_letters(item)

print('''Input file contains:
%i letters
%i words
%i lines''' % (ans['letters'], ans['words'], ans['lines']))
