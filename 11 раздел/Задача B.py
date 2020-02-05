# В бинарном алгоритме Евклида не используются операции деления и остатка, а используется только # проверка на чётность и деление на 2. Идея бинарного алгоритма Евклида следующая:# \(НОД(a,b)=2НОД(a/2,b/2)\), если \(a\) и \(b\) четные,# \(НОД(a,b)=НОД(a/2,b)\), если \(a\) четное, \(b\) нечетное,# \(НОД(a,b)=НОД(a,b/2)\), если \(a\) нечетное, \(b\) четное,# \(НОД(a,b)=НОД(a-b,b)\), если \(a\) и \(b\) нечетные, \(a\ge b\).

a = int(input())
b = int(input())

def divide_to_min(num):
    while num % 2 == 0:
        num /= 2
    return num

def algo(a, b):
    k = 1

    while b != a and a != 0:
        a_2 = a % 2
        b_2 = b % 2
        if a_2 == 0 and b_2 == 0:
            while a % 2 == 0 and b % 2:
                a /= 2
                b /= 2
                k *= 2
        elif a_2 == 0 and b_2 != 0:
            a = divide_to_min(a)
        elif b_2 == 0 and a_2 != 0:
            b = divide_to_min(b)
        if a >= b:
            a -= b
        else:
            b -= a
    return b * k

print(int(algo(a, b)))