# По данным целым неотрицательным \(n\) и \(k\) вычислите значение числа сочетаний из \(n\) элементов по \(k\),
# то есть \(\frac{n!}{k!(n-k)!}\).

import math

n = int(input())
k = int(input())

print(math.factorial(n) // (math.factorial(k) * math.factorial(n - k)))
