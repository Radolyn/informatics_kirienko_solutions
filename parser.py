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
except:
    print('Запустите сначала deps.py - установите зависимости.')
    exit(3)

# Этот скрипт парсит последний удачный run по problem_id, извлекает из него сурсы и создаёт файл с решением
# API у них не задокументировано *(я нашёл роуты, но не более: https://github.com/InformaticsMskRu/informatics-mccme-ru/blob/master/pynformatics/__init__.py), так что парсим 'грязно'

if len(sys.argv) != 6:
    print('Использование: parser.py startid endid userid folder modulesession\nДля получения modulesession запустите getKey.py')
    exit(2)

start_id = int(sys.argv[1])
end_id = int(sys.argv[2])
user_id = sys.argv[3]
folder = sys.argv[4]

# Селектор

desc_selector = '#content > table > tbody > tr:nth-child(2) > td:nth-child(2) > div > div > div:nth-child(11) > div.legend > p'

# Нет бы сделать какой-нибудь API-key, мы лучше сделаем проверку авторизацию по кукам!

cookies = {
    'MoodleSession': sys.argv[5]
}

# Заголовки

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

# Выводит все json ответы

debug = False

# Все букОвки от A до AZ (не бойтесь, я их сгенерировал за 3 строчки :D)

letters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AM', 'AN', 'AO', 'AP', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AV', 'AW', 'AX', 'AY', 'AZ']

# Сколько всего скачано

passes = 0


print('''\
 _____       __                           _   _          
|_   _|     / _|                         | | (_)         
  | | _ __ | |_ ___  _ __ _ __ ___   __ _| |_ _  ___ ___ 
  | || '_ \|  _/ _ \| '__| '_ ` _ \ / _` | __| |/ __/ __|
 _| || | | | || (_) | |  | | | | | | (_| | |_| | (__\__ \\
 \___/_| |_|_| \___/|_|  |_| |_| |_|\__,_|\__|_|\___|___/ parser by AlexeyZavar (1.0)
                                                         
                                                         
                                                         ''')


for i in range(start_id, end_id + 1, 1):

    problem_id = i
    letter = letters_list[i - start_id]

    url = 'https://informatics.mccme.ru/py/problem/%s/filter-runs?problem_id=%s&from_timestamp=-1&to_timestamp=-1&group_id=0&user_id=%s&lang_id=-1&status_id=-1&statement_id=0&count=10&with_comment=&page=1' % (
        problem_id, problem_id, user_id)

    response = requests.get(url, cookies=cookies)
    data = json.loads(response.text)

    if not os.path.exists(folder):
        os.makedirs(folder)

    if debug:
        print(response.text)
    if (data['result'] != 'success'):
        print('Прикол не работает, идём дальше')
        continue

    print('Прикол работает')

    print('Получаем удачные run\'ы...')

    success_runs = list()

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

    source_url = 'https://informatics.mccme.ru/py/problem/run/%i/source' % run['id']

    response = requests.get(source_url, cookies=cookies)
    data = json.loads(response.text)


    if debug:
        print(response.text)
    if data['status_code'] != 200:
        print('Ставлю дизлайк и идём дальше\n\n')
        continue

    print('Ставлю лайк')

    source = data['data']['source']

    if debug:
        print(source)

    desc_url = 'https://informatics.mccme.ru/mod/statements/view3.php?id=%s' % problem_id

    page = requests.get(desc_url)

    soup = BeautifulSoup(page.text, 'lxml')
    if debug:
        print(soup)

    desc = soup.find('div', {'class': 'legend'})

    if desc == None:
        print('Ржомба не сработала, продолжаем флексить')
        desc_url = 'https://informatics.mccme.ru/mod/statements/view3.php?chapterid=%s' % problem_id

        page = requests.get(desc_url)

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

    f = open(folder + "\Задача %s.py" % letter, "w+", encoding='utf-8', newline='')

    f.write('# ')
    f.write(desc.replace('\n', '# '))
    f.write('\n\n')
    f.write(source.replace('\r\n', '\n'))

    f.close()

    print('Класс работает, ставлю ржомбу. (%s, %i)\n\n' % (letter, problem_id))

    passes += 1

    # Автозагрузчик заданий потом сделаем
    # '/py/problem/problem_id/submit'

print('\n\nПриколов скачано: ' + str(passes) + ' из ' + str(abs(start_id - end_id) + 1))