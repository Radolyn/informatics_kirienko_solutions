# 		В олимпиаде участвовало $N$ человек. Каждый получил определенное количество баллов, при этом оказалось,что у всех участников — разное число баллов.
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

a, b = list(), list()

c = informatics.getInput()

for i in range(0, c, 1):
    d, f = map(str, input().split())
    a.append(d)
    b.append(int(f))

l = len(a)

for j in range(0, l, 1):
    n = b.index(max(b))
    print(a[n])
    a.remove(a[n])
    b.remove(max(b))
