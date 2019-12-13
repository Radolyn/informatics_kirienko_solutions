# Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю.# Помогите ему это сделать.

inputList = input().split()
b = int(input())

c = 0

for i in range(0, len(inputList)):
    d = int(inputList[i])
    if d >= b:
        c = i + 1
print(c + 1)
