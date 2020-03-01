# Даны длины сторон треугольника. Вычислите площадь треугольника.

import math

a = float(input())
b = float(input())
c = float(input())

p = (
    a + b + c
) / 2  # https://ru.onlinemschool.com/math/assistance/figures_area/triangle1/

s = (p * (p - a) * (p - b) * (p - c)
     )  # https://ru.onlinemschool.com/math/assistance/figures_area/triangle1/

if s < 0:
    s *= -1

print('{:.6f}'.format(pow(s, 0.5)))
