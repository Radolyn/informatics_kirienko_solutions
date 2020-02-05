import getopt
import json
import pickle
import sys


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
    sys.exit(2)


def get_user_details(session):
    response = session.get('https://informatics.mccme.ru/py/rating/get', cookies=load_cookies())
    return json.loads(response.text)['current_user_data']


def save_cookies(requests_cookiejar):
    with open('session', 'wb') as (f):
        pickle.dump(requests_cookiejar, f)


def load_cookies():
    with open('session', 'rb') as (f):
        return pickle.load(f)
