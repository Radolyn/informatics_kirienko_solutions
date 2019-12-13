# Дано натуральное число N. Выведите слово YES, если число N является# точной степенью двойки, или слово NO в противном случае.

n = int(input())

d = 1

if n == 0 or n == 1:
    print('YES')
    exit(0)

while d <= n:
    d *= 2
    if d == n:
        print('YES')
        exit(0)
print('NO')