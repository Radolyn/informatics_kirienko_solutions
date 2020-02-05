# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.

a, b, c, d, e, f = int(input()), int(input()), int(
    input()), int(input()), int(input()), int(input())

# резултат (логычна)
result = 0

# проверка
check = (a // d) * (b // e) * (c // f)

if check > result:
    result = check
check = (a // d) * (b // f) * (c // e)

if check > result:
    result = check
check = (a // e) * (b // d) * (c // f)

if check > result:
    result = check
check = (a // e) * (b // f) * (c // d)

if check > result:
    result = check
check = (a // f) * (b // d) * (c // e)

if check > result:
    result = check
check = (a // f) * (b // e) * (c // d)

if check > result:
    result = check

print(result)
