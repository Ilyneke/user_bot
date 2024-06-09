# Воронка-вебинар

## Первый запуск:
0. Получаем API_ID и API_HASH для авторизации.\
инструкция: https://core.telegram.org/api/obtaining_api_id
1. Запускаем базу данных:\
`docker-compose up postgres -d`
2. Вводим наши API_ID и API_HASH в файл src/settings/base.py
3. Запускаем скрипт app.py в папке src:\
`python src/app.py`
4. Вводим в консоль номер телефона и код.
5. Проверяем, что рядом с файлом app.py появился новый файл под названием в формате username.session
6. После этого можем  запустить контейнер user_bot

## Последующие запуски:
`docker-compose up -d`
