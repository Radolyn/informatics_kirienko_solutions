# Даны два натуральных числа \(n\) и \(m\). Сократите дробь \(\frac{n}{m}\), то есть выведите два
# других числа \(p\) и \(q\) таких, что \(\frac{n}{m}=\frac{p}{q}\) и дробь \(\frac{p}{q}\) — несократимая.

import math


def ReduceFraction(n, m):
    z = math.gcd(n, m)

    n //= z
    m //= z
    return (n, m)


a, b = int(input()), int(input())

print(*ReduceFraction(a, b))
