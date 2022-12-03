# scrapy_parser_pep

### О проекте
Проект представляет собой асинхронный  парсер веб-сайта python.org. Проект реализован в рамках курса [Практикум.Яндекс](https://practicum.yandex.ru/profile/python-developer-plus/).

# Используемые технологии
[python](https://www.python.org/)
[scrapy](https://docs.scrapy.org/en/latest/)

# Установка проекта 
Склонируйте проект на локальную машину.
```sh
git clone git@github.com:WayBro-54/scrapy_parser_pep.git
```
# Установка виртуального окружения и зависимостей
Создаем виртуальное окружение в папке проекта.
```sh
  python -m venv venv # Для пользователей Windows
  python3 -m venv venv # Для пользователей Linux
```
Активируйте виртуальное окружение
```sh
  venv/scripts/activate # Для пользователей Windows
  venv/bin/activate # Для пользователей Linux
```
Устанавливаем зависимости
```sh
  pip install -r requirements.txt
```

## Запуск программы

выполните команду
```sh
scrapy crawl pep 
```
В репозитории results появится 2 файла.
в первом файле описание Pep: имя, номер, статус
во втором файле общие сводки по количеству статусов. 