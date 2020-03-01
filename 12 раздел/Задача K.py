# После затянувшегося совещания директор фирмы решил заказать такси,чтобы развезти сотрудников по домам. Он заказал N машин —ровно столько, сколь у него сотрудников.Однако когда они подъехали, оказалось, что у каждого водителя такси свой тариф за 1 километр.
# 

class informatics:
    @staticmethod
    def getInput():
        return int(input())

    @staticmethod
    def getMultiInputList():
        return list(map(int, input().split()))

    @staticmethod
    def getMultiInputOneLine():
        return map(int, input().split())

    @staticmethod
    def SelectionSort(l):
        length = len(l)
        for i in range(length - 1):
            m = i
            j = i + 1
            while j < length:
                if l[j] < l[m]:
                    m = j
                j += 1
            l[i], l[m] = l[m], l[i]
        return l

    @staticmethod
    def InsertionSort(l):
        k = list()
        while l:
            f = l.pop()
            while k and k[-1] > f:
                l.append(k.pop())
            k.append(f)
        return k

    @staticmethod
    def BubbleSort(a):
        length = len(a)
        for i in range(length - 1):
            for j in range(length - i - 1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
        return a

    @staticmethod
    def CountSort(A):
        length = max(A) + 1
        b = [0] * length
        for i in A:
            b[i] += 1
        A[:] = []
        for i in range(length):
            A += [i] * b[i]
        return A


a = informatics.getMultiInputList()
b = informatics.getMultiInputList()

c = 0

length = len(a)

for i in range(0, length):
    ma = max(a)
    mb = min(b)

    c += ma * mb

    a.remove(ma)
    b.remove(mb)

print(c)
