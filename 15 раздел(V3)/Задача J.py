# Дан файл. Определите сколько в нем букв (латинского алфавита), слов, строк. Выведите три найденных числа в формате, приведенном в примере.
def CountWords(a):
    b = 1
    g = 0
    d = -1
    a = list(a)
    for i in range(len(a)):
        if 64 < int(ord(a[i])) < 91 or 96 < int(ord(a[i])) < 123:
            g += 1 
    if g > 1:
        while not(a[d].isalpha()):
            del a[d]
        a = "".join(a)
        for i in range(1, len(a)):
            if a[i - 1].isalpha() and a[i] == '-' and a[i + 1].isalpha():
                pass
            elif a[i - 1].isalpha() and not(a[i].isalpha()):
                b += 1
        return b
    elif g == 1:
        return 1
    else:
        return 0
f = open('input.txt')
s = f.readlines()
a = 0
b = 0
for i in range(len(s)):
    for j in range(len(s[i])):
        if s[i][j].isalpha():
            a += 1
    b += CountWords(s[i])
print("Input file contains:")
print(str(a), "letters")
print(str(b + 1), "words")
print(str(len(s)), "lines")
f.close()
