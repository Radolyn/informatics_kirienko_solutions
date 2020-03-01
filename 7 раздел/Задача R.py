# Последовательность Фибоначчи определяется так:
# \[
# \varphi_0=0, \varphi_1=1, ..., \varphi_{n}=\varphi_{n-1}+\varphi_{n-2}.
# \]
# 

f1 = 1
f2 = 1

n = int(input())

i = 0

while i < n - 2:
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    i = i + 1

print(f2)
