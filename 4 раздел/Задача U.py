# Даны два четырёхзначных числа A и B. Выведите все четырёхзначные числа на отрезке от A до B, запись которых
# является палиндромом.

num1 = int(input())
num2 = int(input())

print(*[
    x for x in range(num1, num2 + 1)
    if str(x) == str(x)[::-1] and len(str(x)) == 4
],
    sep='\n')
