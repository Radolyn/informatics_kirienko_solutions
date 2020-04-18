# Для поступления в вуз абитуриент должен предъявить результаты трех экзаменов в виде ЕГЭ, каждый из них оценивается целым числом от 0 до 100 баллов. При этом абитуриенты, набравшие менее 40 баллов (неудовлетворительную оценку) по любому экзамену из конкурса выбывают. Остальные абитуриенты участвуют в конкурсе по сумме баллов за три экзамена.
f = open('input.txt')
s = f.readlines()
a = []
for i in range(len(s)):
    a.append(s[i].split())
    for j in range(len(a[i]) - 1, -1, -1):
        if not(a[i][j].isdigit()):
            del a[i][j]
for i in range(len(a) - 1, 0, -1):
    for j in range(len(a[i])):
        if int(a[i][j]) < 40:
            del a[i]
            break
a[0] = int("".join(a[0]))
if len(a) - 1 <= a[0]:
    print(0)
else:
    for i in range(1, len(a)):
        a[i] = int(a[i][0]) + int(a[i][1]) + int(a[i][2])
    a[1:] = sorted(a[1:], reverse = True)
    if a[0] + 1 < len(a) and a[1] == a[a[0] + 1]:
        print(1)
    else:
        b = a[0]
        while a[0] + 1 < len(a) and b != 0 and a[a[0] + 1] == a[b]:
            b -= 1
        print(a[b])
