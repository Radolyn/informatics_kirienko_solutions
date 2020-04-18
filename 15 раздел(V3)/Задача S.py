# В олимпиаде по информатике принимало участие $N$ человек. Определите школы, из которых в олимпиаде принимало участие больше всего участников. В этой задаче необходимо считывать данные построчно, не сохраняя в памяти данные обо всех участниках, а только подсчитывая число участников для каждой школы.
f = open('input.txt')
s = f.readlines()
a = []
b = [0] * 100
for i in range(len(s)):
    s[i] = list(s[i])
    for j in range(len(s[i])):
        if not(s[i][j].isdigit()):
            s[i][j] =  " "
    s[i] = "".join(s[i])
    a.append(s[i].split())
for i in range(len(a)):
    b[int(a[i][0])] += 1
for i in range(len(b)):
    if int(b[i]) == max(b):
        print(i)
