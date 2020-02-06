import getopt
import json
import os
import pickle
import sys

import requests

# Выводит всю отладочную информацию
debug = False

# Заголовки
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/70.0.3538.77 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3',
    # 'Content-Type': 'application/x-www-form-urlencoded',
    'DNT': '1',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://informatics.mccme.ru'
}

# Все букОвки от A до AZ (не бойтесь, я их сгенерировал за 3 строчки :D)
letters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AM',
                'AN', 'AO', 'AP', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AV', 'AW', 'AX', 'AY', 'AZ']


def print_logo():
    print('''\
 _____       __                           _   _          
|_   _|     / _|                         | | (_)         
  | | _ __ | |_ ___  _ __ _ __ ___   __ _| |_ _  ___ ___ 
  | || '_ \|  _/ _ \| '__| '_ ` _ \ / _` | __| |/ __/ __|
 _| || | | | || (_) | |  | | | | | | (_| | |_| | (__\__ \\
 \___/_| |_|_| \___/|_|  |_| |_| |_|\__,_|\__|_|\___|___/ parser by AlexeyZavar (1.2)
                                                         
                                                         
                                                         ''')


def parse_argv(argv):
    try:
        opts, args = getopt.getopt(
            argv, "h",
            ["one=", "letter=", "range=", "folder="])
    except getopt.GetoptError:
        usage()
    params = {'folder': '', 'range': [], 'letter': 'A'}
    for opt, arg in opts:
        if opt == '-h':
            usage()
        elif opt == "--folder":
            params['folder'] = arg
        elif opt == "--one":
            params['range'] = [arg, arg]
        elif opt == "--range":
            params['range'] = arg.split('-')
        elif opt == "--letter":
            params['letter'] = arg
    if params['folder'] == '' or params['range'] == []:
        usage()
    params['range'][0] = params['range'][0].isdigit() and int(params['range'][0]) or usage()
    params['range'][1] = params['range'][1].isdigit() and int(params['range'][1]) or usage()
    return params


def usage():
    print(
        '''
        Использование: parser.py --folder папка_для_сохранения параметры
        Для получения исх. кода на 1 задание следует указать: --one номер_задания --letter буква
        Для получения исх. кодов на несколько заданий следует указать: --range нач_номер-кон_номер --letter нач_буква
        Если --letter не указано, по умолчанию используется A
        '''
    )
    if debug:
        print(sys.argv)
    sys.exit(2)


def get_user_details(session):
    response = session.get('https://informatics.mccme.ru/py/rating/get', cookies=load_cookies())
    return json.loads(response.text)['current_user_data']


def save_cookies(cookies):
    with open('session', 'wb') as (f):
        pickle.dump(cookies, f)


def load_cookies():
    with open('session', 'rb') as (f):
        return pickle.load(f)


def upload(problem_id, file):
    if not os.path.exists(file):
        return False
    with open(file, 'rb') as f:
        headers['Referer'] = 'https://informatics.mccme.ru/mod/statements/view.php?id=' + str(problem_id)
        response = requests.post('https://informatics.mccme.ru/py/problem/' + str(problem_id) + '/submit',
                                 files=dict(file=f), cookies=load_cookies(), headers=headers, data=dict(lang_id=27))
        if debug:
            print(response.text)
        j = json.loads(response.text)
        if debug:
            print(j)
        if j['status'] != 'success':
            return False
        return True
