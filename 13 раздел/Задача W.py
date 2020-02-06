# 		Хорошо известна задача-шутка, в которой требуется продолжить числовой ряд:
# 


y = int(input())


def Yes(n):
    p = "1"
    seq = [1]
    while n > 1:
        q = ''
        index = 0
        length = len(p)
        while index < length:
            start = index
            index += 1
            while index < length and p[index] == p[start]:
                index += 1
            q += str(index - start) + p[start]
        n, p = n - 1, q
        seq.append(int(p))
    return seq


print(Yes(y)[y - 1])
