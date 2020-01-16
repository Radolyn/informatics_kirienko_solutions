# # 		Дан список целых чисел.Выведите все элементы этого списка в порядке невозрастания значений.Выведите новый список на экран.#  

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

l = informatics.getMultiInputList()

# Здравстуйте ******** ********, я рад Вас видеть в своём коде и надеюсь у вас хорошее настроение.
print(*reversed(informatics.SelectionSort(l)))