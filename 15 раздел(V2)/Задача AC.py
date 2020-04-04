from collections import Counter, OrderedDict
 
 
class OrderedCounter(Counter, OrderedDict):
    pass
 
 
oc = OrderedCounter(l for l in map(str.rstrip, open('input.txt')) 
                        if l not in ('PARTIES:', 'VOTES:'))
votes = sum(oc.values()) - len(oc)
print('\n'.join(str(p) for p in oc if (oc[p] - 1) / votes >= 0.07))