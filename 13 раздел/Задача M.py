# В шифре Цезаря каждый символ заменяется на другой символ, третий по счету в алфавите после данного, с цикличность. То есть символ A заменяется на D, символ B - на E, символ C - на F, ..., символ Z на C. Аналогично строчные буквы заменяются на строчные буквы. Все остальные символы не меняются. 

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def CaesarCipherChar(c, k):
    d = alphabet.find(c)
    l = len(alphabet) // 2
    if d < l and c in alphabet:
        l *= 2
        if c.islower():
            return alphabet[d + k].lower()
        else:
            return alphabet[d + k].upper()
    elif c not in alphabet:
        return c
    if c.islower():
        return alphabet[d + k - l].lower()
    else:
        return alphabet[d + k - l].upper()


def CaesarCipher(s, k):
    for item in s:
        yield CaesarCipherChar(item, k)


res = CaesarCipher(input(), 3)

for item in res:
    print(item, end='')
