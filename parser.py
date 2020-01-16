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
    from utils import parse_argv, usage, get_user_details, load_cookies
except:
    print('Запустите сначала deps.py - установите зависимости')
    exit(3)

# Этот скрипт парсит последний удачный run по problem_id, извлекает из него сурсы и создаёт файл с решением
# API у них не задокументировано *(я нашёл роуты, но не более: https://github.com/InformaticsMskRu/informatics-mccme-ru/blob/master/pynformatics/__init__.py), так что парсим 'грязно'

# Выводит всю отладочную информацию

debug = False

# Парсим аргументы из ком. строки
parsed = parse_argv(sys.argv[1:])

if debug:
    print(parsed)

start_id = parsed['range'][0]
end_id = parsed['range'][1]
folder = parsed['folder']

# Селектор

desc_selector = '#content > table > tbody > tr:nth-child(2) > td:nth-child(2) > div > div > div:nth-child(11) > div.legend > p'

# Заголовки

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'DNT': '1',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://informatics.mccme.ru'
}

# Все букОвки от A до AZ (не бойтесь, я их сгенерировал за 3 строчки :D)

letters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AM', 'AN', 'AO', 'AP', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AV', 'AW', 'AX', 'AY', 'AZ']

# Сколько всего скачано

passes = 0

# Сессия для парсера

session = requests.Session()



print('''\
 _____       __                           _   _          
|_   _|     / _|                         | | (_)         
  | | _ __ | |_ ___  _ __ _ __ ___   __ _| |_ _  ___ ___ 
  | || '_ \|  _/ _ \| '__| '_ ` _ \ / _` | __| |/ __/ __|
 _| || | | | || (_) | |  | | | | | | (_| | |_| | (__\__ \\
 \___/_| |_|_| \___/|_|  |_| |_| |_|\__,_|\__|_|\___|___/ parser by AlexeyZavar (1.0)
                                                         
                                                         
                                                         ''')
                                                         

# Создаём папку
if not os.path.exists(folder):
    os.makedirs(folder)

if not os.path.exists('session'):
    print('Запустите сначала getKey.py - получите ключ')
    exit(420)

# Загружаем куки
session.cookies = load_cookies()

# Проверка на валидность
userdata = get_user_details(session)

if parsed['letter'] not in letters_list:
    print('Хайповая буква, но максимум AZ')
    exit(68)

letter_offset = letters_list.index(parsed['letter'])

if userdata == None:
    print('Токен истёк или невалиден. Получите новый с помощью getKey.py')
    exit(4)

print('Доброго времени суток, ' + userdata['name'])
print('Произошла авторизация, идём к выкачке\n\n')

user_id = userdata['id']

# Главный кос... цикл
for i in range(start_id, end_id + 1, 1):

    # Для удобства номер задания обозначим как problem_id, а букву - letter
    problem_id = i
    letter = letters_list[i - start_id + letter_offset]

    # Получаем всю информацию по заданию
    url = 'https://informatics.mccme.ru/py/problem/%s/filter-runs?problem_id=%s&from_timestamp=-1&to_timestamp=-1&group_id=0&user_id=%s&lang_id=-1&status_id=-1&statement_id=0&count=10&with_comment=&page=1' % (
        problem_id, problem_id, user_id)

    response = session.get(url, cookies=load_cookies())
    data = json.loads(response.text)

    if debug:
        print(response.text)
    if (data['result'] != 'success'):
        print('Прикол не работает, идём дальше')
        continue

    print('Прикол работает')

    print('Получаем удачные run\'ы...')

    success_runs = list()

    # За выполненное задание дают 100 баллов
    for item in data['data']:
        if item['ejudge_score'] == 100:
            success_runs.append(item)

    if len(success_runs) == 0:
        print('Прикол удачных run\'ов нет\n\n')
        continue

    if debug:
        print(success_runs)

    run = success_runs[0]

    if debug:
        print('Последний удачный:')
        print(run)

    print('Получаем source код...')

    # Парсим исходный код
    source_url = 'https://informatics.mccme.ru/py/problem/run/%i/source' % run['id']

    response = session.get(source_url, cookies=load_cookies())
    data = json.loads(response.text)

    # Если не смогли - идём к след. заданию
    if debug:
        print(response.text)

    if data['status_code'] != 200:
        print('Ставлю дизлайк и идём дальше\n\n')
        continue

    print('Ставлю лайк')

    source = data['data']['source']

    if debug:
        print(source)

    # Парсим описание. На самом деле, это для поисковиков, чтобы лучше индексировали :)
    desc_url = 'https://informatics.mccme.ru/mod/statements/view3.php?id=%s' % problem_id

    page = session.get(desc_url)

    soup = BeautifulSoup(page.text, 'lxml')
    if debug:
        print(soup)

    # Описание может быть просто в div'е legend, а может быть обёрнуто в параграф
    desc = soup.find('div', {'class': 'legend'})

    if desc == None:
        print('Ржомба не сработала, продолжаем флексить')
        desc_url = 'https://informatics.mccme.ru/mod/statements/view3.php?chapterid=%s' % problem_id

        page = session.get(desc_url)

        soup = BeautifulSoup(page.content, 'lxml')
        if debug:
            print(soup)
        desc = soup.find('div', {'class': 'legend'}).find('p')

        if desc == None:
            print('Ржомба не сработала, включаем flex air')
            desc = soup.find('div', {'class': 'legend'}).text
            if desc == None:
                print('Ржомба не сработала, вырубаем ютуб\n\n')
                continue
        else:
            desc = desc.text
    else:
        desc = soup.find('div', {'class': 'legend'}).find('p')
        if desc == None:
            desc = soup.find('div', {'class': 'legend'}).text
        else:
            desc = desc.text

    if debug:
        print(desc)

    # Сохраняем описание + исходный код
    f = open(folder + "\Задача %s.py" % letter, "w+", encoding='utf-8', newline='\n')

    #
    f.write('# ')
    # У описания новые строки заменяем на '# ', чтобы было однородней
    f.write(desc.replace('\n', '# '))
    # Костыль.нет
    f.write('\n\n')
    f.write(source.replace('\r\n', '\n'))

    f.close()

    print('Класс работает, ставлю ржомбу. (%s, %i)\n\n' % (letter, problem_id))

    passes += 1

    # Автозагрузчик заданий потом сделаем
    # '/py/problem/problem_id/submit'

print('\n\nПриколов скачано: ' + str(passes) + ' из ' + str(abs(start_id - end_id) + 1))