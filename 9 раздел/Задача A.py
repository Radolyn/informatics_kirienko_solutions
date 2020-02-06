# Выведите все элементы списка с четными индексами
# (то есть A[0], A[2], A[4], ...).


inputList = list(map(int, input().split(" ")))

List = list()

for i in range(0, len(inputList)):
    if i % 2 == 0:
        List.append(inputList[i])

for i in range(0, len(List)):
    print(List[i], end=' ')
