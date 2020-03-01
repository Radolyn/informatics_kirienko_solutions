# В 179 школе есть много коньков самых разных размеров. Школьник может надеть коньки любого размера, который не меньше размеров его ноги. Известны размеры всех коньков и размеры ног школьников. Определите, какое наибольшее число школьников сможет одновременно пойти покататься.


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


a = sorted(informatics.getMultiInputList())
b = sorted(informatics.getMultiInputList())

c = 0

length = len(a)

for i in range(length):
    try:
        if b == []:
            pass
        else:
            f = min(b)
        if f <= a[i] and f in b:
            c += 1
            b.remove(f)
    except BaseException:
        print(0)
        exit()
print(c)
