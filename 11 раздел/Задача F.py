# На клетчатой бумаге нарисовали отрезок из точки с координатами
# \( (a,b)\) в точку с координатами \((c,d)\). Через сколько клеток проходит этот отрезок
# (считается, что отрезок проходит через клетку, если он проходит через ее внутренность,
# если же он проходит только через вершину или по границе клетки, считается, что он не проходит через клетку).
#    


class informatics:
    @staticmethod
    def getInput():
        return int(input())

    @staticmethod
    def getMultiInput():
        return map(int, input().split())


x, y, x2, y2 = informatics.getMultiInput()

m = abs(x - x2)
n = abs(y - y2)
s = m + n

while n != 0 and m != 0:
    if n > m:
        n %= m
    else:
        m %= n
t = m + n
s -= t
print(s)
