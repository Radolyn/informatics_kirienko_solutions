# Определите $N=100000$ и создайте массив [True] * ($N + 1$).Заполните его значениями так, чтобы IsPrime[$i$] == True, если $i$ —простое число и IsPrime[$i$] == False, если $i$ — составное.
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
    def Resheto():
        N = 100000
        s = set(range(1, N, 2))
        for i in range(2, int(N**.5)):
            if i in s:
                s -= set(range(i * i, N, i))
        return s


er = list(informatics.Resheto())
er.insert(1, 2)

n = int(input())

print(er[n])
