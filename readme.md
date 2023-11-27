# Приложение (API) для учёта трат пользователя

## Документация
В процессе написания :)

## Старт проекта

Создать ".env" файл с ".env.example" ключами и заполнить их необходимыми значениями.

1. Клонировать репозиторий: \
`git clone <rep>` 

2. Создать виртуальное окружение: \
`python -m venv .myVenv`

3. Активировать виртуальное окружение: \
`..\.myVenv\Scripts\activate.bat`

4. Установить зависимости: \
  `pip install -r requirements.txt -t .myVenv\Lib\site-packages`

5. Создать базу данных postrgeSQL с названием `test`

6. Сделать миграцию базы данных: \
`python manage.py migrate`

<!-- Активировать виртуальное окружение:
'poetry shell'

Применить миграции:
'poetry run python manage.py migrate'

Создать суперпользователя для доступа к панели администратора:
'poetry run python manage.py createsuperuser'

Запуск приложения:
'poetry run python manage.py runserver' -->

## Запуск тестов
Пока отсутствуют

## Панель администратора
'http://localhost:8000/admin/'