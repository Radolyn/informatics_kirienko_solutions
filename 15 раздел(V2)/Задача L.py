# Задача №111337. Максимальный балл по классам
# В олимпиаде по информатике принимало участие несколько человек.
# Победителем олимпиады становится человек, набравший больше всех баллов.
# Победители определяются независимо по каждому классу. Определите
# количество баллов, которое набрал победитель в каждом классе.
# Гарантируется, что в каждом классе был хотя бы один участник.

fil = open('input.txt', 'r')
mma = fil.readlines()
FUCK = []
word = ' 9 '
word1 = ' 10 '
word2 = ' 11 '
worddef = '\n'
g = 1
gg = 1
i = 0
ii = 0
iii = 0
h = 0
hh = 0
hhh = 0
AA = []
BB = []
CC = []
AA1 = []
BB1 = []
CC1 = []
AA2 = []
BB2 = []
CC2 = []
for item in mma:  # 9 no filt
    if word in item:
        AA.append(item[-3:])
for item in mma:  # 10 no filt
    if word1 in item:
        BB.append(item[-3:])
for item in mma:  # 11 no filt
    if word2 in item:
        CC.append(item[-3:])
for i in range(len(AA)):  # 9 filt1
    AA1.append(AA[i].replace('\n', ''))
    i += 1
for ii in range(len(BB)):  # 10 filt1
    BB1.append(BB[ii].replace('\n', ''))
    ii += 1
for iii in range(len(CC)):  # 11 filt1
    CC1.append(CC[iii].replace('\n', ''))
    iii += 1
for h in range(len(AA1)):  # 9 max fit
    AA2.append(AA1[h].replace(' ', ''))
    i += 1
for hh in range(len(BB1)):  # 10 max filt
    BB2.append(BB1[hh].replace(' ', ''))
    hh += 1
for hhh in range(len(CC1)):
    CC2.append(CC1[hhh].replace(' ', ''))
    hhh += 1
a = max(AA2)
b = max(BB2)
c = max(CC2)
if g == gg:
    FUCK.append(a)
    FUCK.append(b)
    FUCK.append(c)
print(*FUCK)
