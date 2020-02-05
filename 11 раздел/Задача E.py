# Даны две дроби \(\frac ab\) и \(\frac cd\) (числа \(a\) и \(c\) — целые, \(b\) и \(d\) — натуральные).
# Вычислите их сумму и запишите ее в виде смешанной дроби \(x\frac yz\) (число \(x\) целое,
# числа \(y\) и \(z\) натуральные, дробь \(\frac yz\) — правильная несократимая).

import math

a, b, c, d = map(int, input().split(' '))

x = a * d + b * c
y = b * d
z = math.gcd(x, y)

x //= z
y //= z

r = 0

if abs(x / y) >= 1:
    r = abs(x) // abs(y)
    if x < 0:
        x += abs(r) * abs(y)
    else:
        x -= abs(r) * abs(y)

if y < 0 and x > 0:
    y = abs(y)
    x -= x * 2
elif y < 0 and r != 0:
    y = abs(y)
    if r < 0:
        r = abs(r)
    else:
        r -= r * 2

if x < 0 and r > 0:
    x = abs(x)
    r -= r * 2

if r != 0 and x != 0:
    print(r, str(x) + '/' + str(y))
elif r != 0:
    print(r)
elif x != 0:
    print(str(x) + '/' + str(y))
else:
    print(0)
