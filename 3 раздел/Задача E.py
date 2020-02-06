# Даны три целых числа. Найдите наибольшее из них (программа должна вывести ровно одно целое число).
# 


a = int(input())
b = int(input())
c = int(input())

m = a if a > b else b
print(m if m > c else c)
