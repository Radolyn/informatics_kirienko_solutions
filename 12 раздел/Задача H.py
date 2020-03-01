# Системный администратор вспомнил, что давно не делал архива пользовательских файлов.Однако, объем диска, куда он может поместить архив, может быть меньше чем суммарный объем архивируемых файлов.
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


a, b = informatics.getMultiInputOneLine()

yes = list()

for i in range(1, b + 1, 1):
    yes.append(informatics.getInput())

yes = informatics.InsertionSort(yes)

counter = 0

for item in yes:
    if a - item >= 0:
        a -= item
        counter += 1
    else:
        break

print(counter)
