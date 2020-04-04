# «адача є111341. ћаксимальный балл не-победител€
# «ачет проводитс€ отдельно в каждом классе. ѕобедител€ми олимпиады станов€тс€ школьники, которые набрали наибольший балл среди всех участников в данном классе.
# ƒл€ каждого класса определите максимальный балл, который набрал
# школьник, не ставший победителем в данном классе.

fil = open('input.txt', 'r')
file = fil.readlines()
A, B, C = [], [], []
COMPLETE = []
A1, B1, C1 = [], [], []
A12, B12, C12 = [], [], []
for item in file:
    a = list(item.split())
    if a[2] == '9':
        A.append(int(a[3]))
    elif a[2] == '10':
        B.append(int(a[3]))
    else:
        C.append(int(a[3]))
A1 = sorted(A, key=int)
B1 = sorted(B, key=int)
C1 = sorted(C, key=int)

a1 = A1.index(max(A1)) - 1
b1 = B1.index(max(B1)) - 1
c1 = C1.index(max(C1)) - 1

a12 = A1.index(max(A1))
b12 = B1.index(max(B1))
c12 = C1.index(max(C1))

for a1 in range(len(A1)):
    if A1[a1] < A1[a12]:
        A12.append(A1[a1])
    else:
        a1 -= 1

for b1 in range(len(B1)):
    if B1[b1] < B1[b12]:
        B12.append(B1[b1])
    else:
        b1 -= 1

for c1 in range(len(C1)):
    if C1[c1] < C1[c12]:
        C12.append(C1[c1])
    else:
        c1 -= 1
print(max(A12), max(B12), max(C12))
