from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass

oc = OrderedCounter(l for l in map(str.rstrip, open('input.txt', 'r', encoding = 'utf8')))

oc_list = list(oc.items())

jj = 0

for item in open('input.txt', 'r', encoding = 'utf8'):
    jj += 1

proh = jj / 2

oc_list.sort(key = lambda x: -1 * x[1])

for i in range(len(oc_list)):
    oc_list[i] = list(oc_list[i])

ans, ans1  = [], []

for k in range(len(oc_list)):
    if oc_list[k][1] > proh:
        ans1.append(oc_list[k][0])
    elif oc_list[k][1] <= proh:
        ans.append(oc_list[k][0])

if len(ans1) != 0:
    print(ans1[0])
else:
    print(ans[0])
    print(ans[1])