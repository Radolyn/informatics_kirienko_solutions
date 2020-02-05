# # 		Дан список. Определите, является ли он монотонно возрастающим(то есть верно ли, что каждый элемент этого списка больше предыдущего).#  

class informatics:
    @staticmethod
    def getInput():
        return int(input())
    
    @staticmethod
    def getMultiInput():
        return list(map(int, input().split()))

l = informatics.getMultiInput()

length = len(l)

for i in range(length - 1):
        if l[i] < l[i+1]:
            continue
        else:
            print('NO')
            exit(0)

print('YES')