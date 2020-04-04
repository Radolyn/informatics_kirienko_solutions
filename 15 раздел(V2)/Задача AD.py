from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass

oc = OrderedCounter(l for l in map(str.rstrip, open('input.txt')) 
                        if l not in ('PARTIES:', 'VOTES:'))

oc_list = list(oc.items())

oc_list.sort(key = lambda x: (-1 * x[1], x[0]))

for g in range(len(oc_list)):
    oc_list[g] = list(oc_list[g])

for i in range(len(oc_list)):
    print(oc_list[i][0], end = '\n')