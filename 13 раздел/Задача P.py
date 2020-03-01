# Капитан Флинт зарыл клад на Острове сокровищ. Он оставил описание, как найти клад. Описание состоит из строк вида: “North 5”, где первое слово – одно из “North”, “South”, “East”, “West”, а второе число – количество шагов, необходимое пройти в этом направлении.
# 

x = 0
y = 0

while True:
    b = input()
    cmd = b.split()
    if b == 'Treasure!':
        print(x, y)
        exit(0)
    val = int(cmd[1])
    if cmd[0] == 'North':
        y += val
    elif cmd[0] == 'South':
        y -= val
    elif cmd[0] == 'East':
        x += val
    elif cmd[0] == 'West':
        x -= val
