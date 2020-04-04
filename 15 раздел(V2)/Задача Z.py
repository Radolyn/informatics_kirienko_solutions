from collections import Counter, OrderedDict
 
 
class OrderedCounter(Counter, OrderedDict):
    pass
 
fil = open('input.txt', 'r', encoding = 'utf8')

file = fil.readlines()

ans = []

for item in file:
    a = list(item.split())
    ans.append(int(a[2]))

list_ans_OC = list(OrderedCounter(ans).items())

list_ans_OC.sort(key = lambda x: (-1 * x[1], x[0]))

for n in range(len(list_ans_OC)):
    list_ans_OC[n] = list(list_ans_OC[n])

for k in range(len(list_ans_OC)):
    print(list_ans_OC[k][0], end = ' ')

fil.close()