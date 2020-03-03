try:
    import requests
    import sys
    import pickle
    from utils import save_cookies, debug, headers
except:
    from utils import deps_message

    deps_message()

if len(sys.argv) != 3:
    print(
        'Использование: authorize.py login password.\n'
        'Ваши данные никуда не отправляются, кроме костыльного сервера informatics.')
    exit(2)

with requests.Session() as session:
    session.post('https://informatics.mccme.ru/login/index.php',
                 data={'username': sys.argv[1].lower(), 'password': sys.argv[2]}, headers=headers)

    response = session.get('https://informatics.mccme.ru/login/index.php')

    if 'Вы зашли под именем' in response.text:
        print('Авторизация сохранена. Теперь можно пользоваться парсером!')
        if debug:
            print(session.cookies['MoodleSession'])
        save_cookies(session.cookies)
        exit(0)

print('Неверный логин или пароль. Ну или сервер упал.')
exit(1)
