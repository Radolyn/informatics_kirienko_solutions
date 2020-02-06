# Даны два целых числа A и B (при этом A≤B). Выведите все числа от A до B включительно.
#    



a, b = int(input()), int(input())

for i in range(a, b):
    print(i)
print(b)
