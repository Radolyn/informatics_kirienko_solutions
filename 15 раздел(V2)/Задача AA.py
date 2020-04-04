fil = open('input.txt', 'r', encoding = 'utf8')
file = fil.readlines()

ans = []

for i in range(100):
    ans.append([0, 0])

for line in file:
    line = list(line.split()[2:])
    ans[int(line[0])][0]+= int(line[1])
    ans[int(line[0])][1] += 1

d = {}

for h in range(100):
    if ans[h][0] != 0:
        d[h] = ans[h][0] / ans[h][1]

d_list = list(d.items())

d_list.sort(key = lambda x: (-1 * x[1], x[0]))

for g in range(len(d_list)):
    d_list[g] = list(d_list[g])

COMPLETE = []

for l in range(len(d_list)):
    COMPLETE.append(d_list[l][0])

for item in file:
    a = list(item.split()[2:])
    if a[0] == '1' and a[1] == '0':
        COMPLETE.append(a[0])

for kk in range(len(COMPLETE)):
    print(COMPLETE[kk], end = ' ')