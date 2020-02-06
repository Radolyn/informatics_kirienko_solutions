# Дано натуральное число \(N>1\).
# Выведите все его простые натуральные делители с учетом кратности. Алгоритм должен иметь сложность \(O(\sqrt{n})\).


def isPrime(n):
    if n == 2:
        return True
    i = 2
    while n % i != 0:
        i += 1
        if i ** 2 > n:
            return True
    return False


n = int(input())

while n != 1:
    for i in range(2, int(n ** .5) + 1, 1):
        if isPrime(i) and n % i == 0:
            print(i, end=' ')
            n //= i
            break
    else:
        print(n, end=' ')
        break
