# В файле могут быть записаны десятичные цифры и все, что угодно. Числом назовем последовательность цифр, идущих подряд (т.е. число всегда неотрицательно). 
f = open('input.txt')
s = f.readlines()
a = 0
for i in range(len(s)):
    for j in range(len(s[i])):
        if not(s[i][j].isdigit()):
            s[i] = s[i].replace(s[i][j]," ")
s = "".join(s)
s = s.split()
for i in range(len(s)):
    a += int(s[i])
print(a)
f.close()
