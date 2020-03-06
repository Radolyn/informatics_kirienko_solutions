# Зашифруйте данный текстовый файл шифром Цезаря, при этом символы первой строки файла должны циклически сдвигаться на 1, второй строки — на 2, третьей строки — на три и т.д.
#  

import re

f = open('input.txt', 'r')

data = f.readlines()

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def CaesarCipherChar(c, k):
    d = alphabet.find(c.lower())
    l = len(alphabet) // 2
    if d < l and c in alphabet:
        l *= 2
        if c.islower():
            return alphabet[(d + k) % len(alphabet)].lower()
        else:
            return alphabet[(d + k) % len(alphabet)].upper()
    elif c not in alphabet:
        return c
    if c.islower():
        return alphabet[d + k - l].lower()
    else:
        return alphabet[d + k - l].upper()


def CaesarCipher(s, k):
    for item in s:
        yield CaesarCipherChar(item, k)


ans = []

i = 0

for item in data:
    i += 1
    print(*CaesarCipher(item[:-1], i), sep='')
