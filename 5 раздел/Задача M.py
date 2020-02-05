# По данному числу n вычислите сумму
# \(1+\frac{1}{2^2}+\frac{1}{3^2}+...+\frac{1}{n^2}\).

n = int(input())

a = 0

for i in range(1, n + 1):
    a += 1 / i ** 2

print(a)
