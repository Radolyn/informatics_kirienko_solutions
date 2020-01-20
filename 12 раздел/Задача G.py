# # 		Дан список целых чисел. Отсортируйте его в порядке невозрастания значений. Выведите полученный список на экран.#   

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
        for i in range(length-1):
            for j in range(length-i-1):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
        return a
    
# Zdarova
print(*reversed(informatics.BubbleSort(informatics.getMultiInputList())))
