# 
# 		Хорошо известна задача-шутка, в которой требуется продолжить числовой ряд:
# 

e = int(input())


def Eval(n):
    p = "1"
    seq = [1]
    while (n > 1):
        q = ''
        index = 0
        length = len(p)
        while index < length:
            start = index
            index += 1
            while index < length and p[index] == p[start]:
                index += 1
            q = q + str(index - start) + p[start]
        n, p = n - 1, q
        seq.append(int(p))
    return seq


print(Eval(e)[e - 1])
