try:
    import requests
    import sys
    import pickle
    from utils import save_cookies, debug
except:
    print('Запустите сначала deps.py - установите зависимости.')
    exit(3)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Content-Type': 'application/x-www-form-urlencoded',
    'DNT': '1',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://informatics.mccme.ru'
}

if len(sys.argv) != 3:
    print(
        'Использование: getKey.py login password\nВаши данные никуда не отправляются, кроме костыльного сервера informatics.')
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
