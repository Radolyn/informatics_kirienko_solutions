# А вот другой ряд, в котором вычисляется значение дзета-функции для числа 2:
# \[
# \frac{\pi^2}{6} = \frac{1}{1^2}+\frac{1}{2^2}+\frac{1}{3^2}+\frac{1}{4^2}+ ...
# \]
# 

import math

terms = 10

a = 0
for i in range(1, terms + 1):
    a += 1 / i ** 2
b = math.sqrt(6 * a)
print(b)
