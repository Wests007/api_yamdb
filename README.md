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
git clone https://github.com/Wests007/api_yamdb.git
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
cd api_yamdb
```

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

### Документация запросов к API доступна после запуска сервера по адресу:

```
127.0.0.1:8000/redoc
```

### Регистрация пользователя и получение токена:

- Регистрация

POST /api/v1/auth/signup/
```
{
    "email": "string",
    "username": "string"
}
```

- Получение токена

POST /api/v1/auth/token/
```
{
    "username": "string",
    "confirmation_code": "string"
}
```

- Редактирование пользовательского профиля

PATCH /api/v1/users/me/
```
{
    "username": "string",
    "email": "user@example.com",
    "first_name": "string",
    "last_name": "string",
    "bio": "string"
}
```

### Примеры некоторых запросов к API:

- Получение списка всех категорий

GET /api/v1/categories/
```
[
    {
        "count": 0,
        "next": "string",
        "previous": "string",
        "results":
            [
                {
                    "name": "string",
                    "slug": "string"
                }
            ]
    }
]
```

- Получение списка всех жанров

GET /api/v1/genres/
```
[
    {
        "count": 0,
        "next": "string",
        "previous": "string",
        "results":
            [
                {
                    "name": "string",
                    "slug": "string"
                }
            ]
    }
]
```

- Добавление нового отзыва

POST /api/v1/titles/{title_id}/reviews/
```
{
    "text": "string",
    "score": 1
}
```

- Добавление комментария к отзыву

POST /api/v1/titles/{title_id}/reviews/{review_id}/comments/
```
{
    "text": "string"
}
```

## Авторы проекта:
[Асеев Александр](https://github.com/VANGAZOR)
[Гриднев Кирилл](https://github.com/Keyreall96)
[Ромашков Александр](https://github.com/Wests007)
