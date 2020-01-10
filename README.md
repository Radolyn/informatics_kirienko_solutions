# Informatics ответы

## Решения
Решения задач авторского курса Д. П. Кириенко. с informatics.mccme.ru

## Парсер
Чтобы не копировать код и описание с сайта, был сделан парсер.

Для его работы необходимо установить зависимости:
```sh
pip install bs4
pip install requests
pip install lxml
```

Использование: ```python parser.py startid endid userid folder modulesession```

**startid и endid** - начальный и конечный id'шники. Можете сами достать из адресной строки *(```/view3.php?chapterid=3828```)* или из таблицы ниже.

**userid** - id пользователя. Кликаете по своему имени справа вверху страницы -> в адресной строке ищете ```/view.php?id=135012``` *(135012 - id)*.

**folder** - название папки, куда сохранить все ваши решения (п. - '1 раздел') ***в кавычках***.

**modulesession** - рандомная строка из куки. Вы должны скачать расширение EditThisCookie и получить значение 'MoodleSession'.

### Таблица startid и endid по разделам

| 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 10   | 11*  | 12     | 13     | 14.1   | 14.2   | 15     | 16** |
|------|------|------|------|------|------|------|------|------|------|------|--------|--------|--------|--------|--------|------|
| 3443 | 3455 | 3501 | 3528 | 3608 | 3735 | 3642 | 3791 | 3828 | 3828 | 4179 | 111152 | 111300 | 111194 | 111362 | 111326 | 3749 |
| 3450 | 3535 | 3527 | 3553 | 3629 | 3748 | 3667 | 3815 | 3853 | 3853 | 4197 | 111177 | 111325 | 111220 | 111387 | 111361 | 3774 |

\* - есть ещё диапазон (112666-112672)

\** - есть ещё номер (113078)

## Участие
Если у вас есть оптимальное решение задачи - можете спарсить его и создать pull request.

## Дисклеймер
Не поленитесь посмотреть на код и разобраться в нём, а не просто копипастить :)
