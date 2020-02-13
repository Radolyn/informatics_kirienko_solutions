# coding=utf-8
# Дева4ки балдеем

try:
    import string
    import requests
    import json
    from operator import attrgetter
    from bs4 import BeautifulSoup
    import lxml
    import sys
    import os
    import pickle
    from utils import parse_argv, usage, get_user_details, load_cookies, debug, headers, letters_list, upload, \
        print_logo, waitS
except:
    print('Запустите сначала deps.py - установите зависимости.')
    exit(3)

# Парсим аргументы из ком. строки
parsed = parse_argv(sys.argv[1:])

# Сколько всего загружено
passes = 0

start_id = parsed['range'][0]
end_id = parsed['range'][1]
folder = parsed['folder']

if parsed['letter'] not in letters_list:
    print('Хайповая буква, но максимум AZ.')
    exit(68)

if not os.path.exists('session'):
    print('Запустите сначала authorize.py - получите ключ.')
    exit(420)

if not os.path.exists(folder):
    print('Папка находится в другой вселенной.')
    exit(96)

letter_offset = letters_list.index(parsed['letter'])

# Сессия для парсера
session = requests.Session()

print_logo()

# Загружаем куки
session.cookies = load_cookies()

# Проверка на валидность
user_data = get_user_details(session)

if user_data is None:
    print('Токен истёк или невалиден. Получите новый с помощью authorize.py')
    exit(4)
    
print('Доброго времени суток, ' + user_data['name'])
print('Произошла авторизация, идём к списыванию.\n\n')

# Главный кос... цикл
for problem_id in range(start_id, end_id + 1, 1):
    # Для удобства обозначим букву как letter
    letter = letters_list[problem_id - start_id + letter_offset]

    path = os.path.abspath(folder) + '\\Задача ' + letter + '.py'

    if not os.path.exists(path):
        print('Решение не найдено, обновите решебник.')
        continue

    res = upload(problem_id, path)

    if not res:
        print('Списание не удалось. Возможно, уже списали.')
        continue

    print('Задача списана успешно. (%s, %i)\n\n' % (letter, problem_id))
    passes += 1
    
    waitS()

print('\n\nПриколов отправлено: ' + str(passes) + ' из ' + str(abs(start_id - end_id) + 1))
