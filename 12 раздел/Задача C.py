# Дана последовательность чисел, состоящая только из чисел 1, ..., 9. Последовательность завершается числом 0. Каждое число записано в отдельной строке.
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


l = [0, 0, 0, 0, 0, 0, 0, 0, 0]

while True:
    s = int(input())
    if s != 0:
        l[s - 1] += 1
    else:
        break

for i in range(len(l)):
    print(l[i], end=' ')
