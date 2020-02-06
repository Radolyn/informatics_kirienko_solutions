# Для данного числа n<100 закончите фразу “На лугу пасется...”
# одним из возможных продолжений: “n коров”, “n корова”, “n коровы”,
# правильно склоняя слово “корова”.



n = int(input())
if n >= 11 and n <= 14:
        print(n, 'korov')
else:
        temp = n % 10
        if temp == 0 or (temp >= 5 and temp <= 9):
                print(n, 'korov')
        if temp == 1:
                print(n, 'korova')
        if temp >=2 and temp <=4:
                print(n, 'korovy')