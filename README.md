# api_yamdb
api_yamdb

### Описание
Самые лучшие и достоверные отзывы на произведения здесь! Простой, надежный и понятный API.

### Технологии
Python 3.7
Django 2.2.19

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone ТУТ АДРЕСА НАШИХ РЕПОЗИТОРИЕВ
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Наполнить БД тестовыми данными возможно командой:

```
python manage.py import_csv_to_db
```

Запустить проект:

```
python manage.py runserver
```

### Ниже все необходимо поправить под данный проект!!!
### Примеры запросов к API:

- Получение публикаций

GET /api/v1/posts/
```
{
    "count": 123,
    "next": "http://api.example.org/accounts/?offset=400&limit=100",
    "previous": "http://api.example.org/accounts/?offset=200&limit=100",
    "results": [
        {...}
    ]
}
```

- Создание публикации

POST /api/v1/posts/

```
{
    "text": "string",
    "image": "string",
    "group": 0
}
```
