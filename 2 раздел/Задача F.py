# Длина Московской кольцевой автомобильной дороги — 109 километров.
# Байкер Вася стартует с нулевого километра МКАД и едет со скоростью \(v\) километров
# в час. На какой отметке он остановится через \(t\) часов?


import math

x, y = int(input()), int(input())
z = (x * y) % 109
print(z)
