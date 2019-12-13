# N школьников делят K яблок поровну, неделящийся остаток остается в корзинке. Сколько яблок достанется каждому школьнику? 

a = 0
b = 0

s = True

l = list()

while s:
    n = int(input())

    if n == 0:
        l.sort()
        l.reverse()
        h = 0
        m = max(l)
        for i in range(0, len(l)):
            if m == l[i]:
                h += 1
        print(h)
        break

    l.append(n)
    b += 1

