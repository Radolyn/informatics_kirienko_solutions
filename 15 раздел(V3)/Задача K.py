# Зашифруйте данный текстовый файл шифром Цезаря, при этом символы первой строки файла должны циклически сдвигаться на 1, второй строки — на 2, третьей строки — на три и т.д. 
f = open('input.txt')
s = f.readlines()
b = 1
for i in range(len(s)):
    a = list(s[i])
    b %= 26
    for j in range(len(a)):
        c = ord(a[j])
        if 64 < c < 91 or 96 < c < 123:
            if c > (90 - b) and c < 91:
                a[j] = chr(c - 26 + b)
            if c > (122 - b) and c < 123:
                a[j] = chr(c - 26 + b) 
            if c <= (90 - b) and c > 64:
                a[j] = chr(c + b)
            if c <= (122 - b) and c > 96:
                a[j] = chr(c + b)
    b += 1
    s[i] = "".join(a)
print(*s,sep = "")
f.close()
