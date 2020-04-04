# «адача є111350. Ўколы с наибольшим средним баллом
# ¬ услови€х предыдущей задачи выведите в пор€дке возрастани€ номера школ,
# средний балл учащихс€ которых максимален (то есть необходимо вычислить
# средний балл дл€ каждой школы и вывести те школы, средний балл дл€
# которых максимален).

fil = open('input.txt', 'r')
ans, AA, COMPLETE = [], [], []
for i in range(100):
    ans.append([0, 0])
h = 0
for line in fil:
    h += 1
    AA.append(int(line.split()[3]))
    line = list(line.split()[2:])
    ans[int(line[0])][0] += int(line[1])
    ans[int(line[0])][1] += 1

sr_max = -1

for k in range(100):
    if ans[k][1] != 0 and (ans[k][0] / ans[k][1]) > sr_max:
        sr_max = (ans[k][0] / ans[k][1])

for l in range(100):
    if ans[l][1] != 0 and (ans[l][0] / ans[l][1]) == sr_max:
        print(l, end=' ')
