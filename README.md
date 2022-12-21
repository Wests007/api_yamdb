# REST API для проекта YaMDb

## Описание
Простой, надежный и понятный API социальной сети с базой данных отзывов к произведениям.

## Технологии
Python 3,
Django 2.2,
Django REST Framework,
Simple-JWT

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
Обновить менеджер пакетов и установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Перейти в папку с файлом manage.py и выполнить миграции:
```
cd api_yamdb
```
```
python manage.py migrate
```
При необходимости, БД возможно наполнить тестовыми данными:
```
python manage.py import_csv_to_db
```
Запустить проект:
```
python manage.py runserver
```

### Полная документация запросов к API доступна после запуска сервера по адресу:
```
127.0.0.1:8000/redoc
```

### Примеры запросов к API:

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

## Авторы:
[Асеев Александр](https://github.com/VANGAZOR),
[Гриднев Кирилл](https://github.com/Keyreall96),
[Ромашков Александр](https://github.com/Wests007)
