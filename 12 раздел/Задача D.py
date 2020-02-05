# # 		Дан список чисел. Определите, есть ли в нем два противоположных(то есть дающих в сумме 0) числа.# # Если такие числа есть в массиве, выведите их индексы в порядке возрастания. Если таких чисел в массиве нет, ничего не выводите. Гарантируется, что таких пар не больше одной.#     

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

l = informatics.getMultiInputList()

for i in range(len(l)):
    m = l[i] * (0-1)
    if m in l:
        index = l.index(m)
        if index > i:
            print(i, index)
        else:
            print(index, i)
        exit(0)
        