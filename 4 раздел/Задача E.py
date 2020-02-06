# По данному натуральном n вычислите сумму 
# \(1^3+2^3+3^3+...+n^3\).


n = int(input())
s = 0
for i in range(n + 1):
    s = s + i * i * i
print(s)
