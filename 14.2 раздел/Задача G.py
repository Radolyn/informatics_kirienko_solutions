# Дано число $n$ и массив размером $n \times n$. Проверьте, является ли этот массив симметричным относительно главной диагонали. Выведите слово “YES”, если массив симметричный, и слово “NO” в противном случае.
# 



def GetCount(n):
    d = [list(map(int, input().split())) for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if d[i][j] == d[j][i] and i != j:
                count += 1
    return count


n = int(input())

c = GetCount(n)
c2 = n ** 2 - n

if c == c2:
    print("YES")
else:
    print("NO")
