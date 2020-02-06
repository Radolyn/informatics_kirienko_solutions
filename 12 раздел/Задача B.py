# 		Найдите наибольшее значение в списке и индекс последнего элемента, который имеет данное значение за один проход по списку, не модифицируя этот список и не используя дополнительного списка.
# 



class informatics:
    @staticmethod
    def getInput():
        return int(input())
    
    @staticmethod
    def getMultiInputList():
        return list(map(int, input().split()))
    
    @staticmethod
    def getMultiInput():
        return map(int, input().split())

l = informatics.getMultiInputList()

m = -1
index = -1

for i in range(len(l)):
    if l[i] >= m:
        m = l[i]
        index = i
print(m, index)
    