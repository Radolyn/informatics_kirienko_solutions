# На склад, который имеет форму прямоугольного параллелепипеда, привезли ноутбуки, упакованные в коробки.
# Каждая коробка также имеет форму прямоугольного параллелепипеда. По правилам хранения коробки с ноутбуками
# должны быть размещены на складе с выполнением следующих двух условий:
# 1. Стороны коробок должны быть параллельны сторонам склада.
# 2. Коробку при помещении на склад разрешается расположить где угодно
# (с выполнением предыдущего условия), в том числе на другой коробке, но все коробки должны быть ориентированы
# одинаково (т.е. нельзя одну коробку расположить “стоя”, а другую —“лежа”)
# 



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
