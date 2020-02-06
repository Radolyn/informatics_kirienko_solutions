# Для настольной игры используются карточки с номерами от 1 до N.
# Одна карточка потерялась. Найдите ее, зная номера оставшихся карточек.



n = int(input())

card = 0

for b in range(1, n + 1):
    card += b

for c in range(n - 1):
    card -= int(input())
print(card)
