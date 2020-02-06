# Даны два действительных числа \(x\) и \(y\). Проверьте, принадлежит ли точка с координатами
# \((x,y)\) заштрихованному квадрату (включая его границу). Если точка принадлежит квадрату, выведите слово YES,
# иначе выведите слово NO. На рисунке сетка проведена с шагом 1.


def IsPointInSquare(x, y):
    r = [round(x * 0.1, 2) for x in range(0, 11)]
    return abs(x) in r and abs(y) in r


res = IsPointInSquare(float(input()), float(input()))

if res:
    print('YES')
else:
    print('NO')
