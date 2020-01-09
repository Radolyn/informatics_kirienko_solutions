# try:
#     import requests
#     import sys
# except:
#     print('Запустите сначала deps.py - установите зависимости.')
#     exit(3)

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'DNT': '1',
#     'Upgrade-Insecure-Requests': '1',
#     'Origin': 'https://informatics.msk.ru'
# }

# if len(sys.argv) != 3:
#     print('Использование: getKey.py login password\nВаши данные никуда не отправляются, кроме костыльного сервера informatics.')
#     exit(2)

# with requests.Session() as session:
#     response = session.post('https://informatics.msk.ru/login/index.php',
#                          data={'username': sys.argv[1],  'password': sys.argv[2]}, headers=headers)

#     #response = session.get('https://informatics.msk.ru/course/view.php?id=156')

#     print(response.text)

#     if 'Вы зашли под именем' in response.text:
#         print(response.cookies.keys())
#         print(response.cookies['MoodleSession'])
#         exit(0)

# print('Неверный логин или пароль. Ну или сервер упал.')

# я чет не понял, сервер куки не возвращает

print('В разработке.')