# Даны действительные коэффициенты \(a\), \(b\), \(c\), при этом \(a\ne0\). Решите квадратное уравнение
# \(ax^2+bx+c=0\) и выведите все его корни. 
#    

import math

a, b, c = float(input()), float(input()), float(input())

d = b**2 - 4 * a * c

if d > 0:
    x1 = (-b + d**0.5) / (2 * a)
    x2 = (-b - d**0.5) / (2 * a)
    if int(x1) == x1:
        x1 = int(x1)
    if int(x2) == x2:
        x2 = int(x2)
    if x2 > x1:
        print(x1, x2)
    else:
        print(x2, x1)
elif d == 0:
    x = -b / (2 * a)
    print(x)
else:
    pass
