from collections import Counter

fil = open('input.txt', 'r', encoding ='utf8')

file = fil.readlines()

AA = []
ans = []

for item in file:
    AA.append(item.split()[2:])
    
max1 = -1

for item in file:
    last_name, first_name, school_number, points = map(
        str, item.replace('\n', '').split())
    if max1 <= int(points):
        max1 = int(points)

for k in range(len(AA)):
    if int(AA[k][1]) == max1:
        ans.append(AA[k])

A = []

for i in range(len(ans)):
    A.append(ans[i][0])  
    
res = []

def most_frequent(A):

    occurence_count = Counter(A)

    return occurence_count.most_common(1)[0][0]

COMPLETE = []

for l in range(len(A)):
    if A.count(most_frequent(A)) == A.count(A[l]):
        COMPLETE.append(A[l])
        
res1 = list(set(COMPLETE))

for ll in range(len(res1)):
    res1[ll] = int(res1[ll])

print(*sorted(res1, key = int))