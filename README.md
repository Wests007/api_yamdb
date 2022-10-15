# api_yamdb
api_yamdb

### ��������
����� ������ � ����������� ������ �� ������������ �����! �������, �������� � �������� API.

### ����������
Python 3.7
Django 2.2.19

### ��� ��������� ������:

����������� ����������� � ������� � ���� � ��������� ������:

```
git clone https://github.com/Wests007/api_yamdb.git
```

```
cd api_yamdb
```

C������ � ������������ ����������� ���������:

```
python -m venv venv
```

```
source venv/scripts/activate
```

���������� ����������� �� ����� requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

��������� ��������:

```
cd api_yamdb
```

```
python manage.py migrate
```

��������� �� ��������� ������� �������� ��������:

```
python manage.py import_csv_to_db
```

��������� ������:

```
python manage.py runserver
```

### ������������ �������� � API �������� ����� ������� ������� �� ������:

```
127.0.0.1:8000/redoc
```

### ����������� ������������ � ��������� ������:

- �����������

POST /api/v1/auth/signup/
```
{
    "email": "string",
    "username": "string"
}
```

- ��������� ������

POST /api/v1/auth/token/
```
{
    "username": "string",
    "confirmation_code": "string"
}
```

- �������������� ����������������� �������

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

### ������� ��������� �������� � API:

- ��������� ������ ���� ���������

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

- ��������� ������ ���� ������

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

- ���������� ������ ������

POST /api/v1/titles/{title_id}/reviews/
```
{
    "text": "string",
    "score": 1
}
```

- ���������� ����������� � ������

POST /api/v1/titles/{title_id}/reviews/{review_id}/comments/
```
{
    "text": "string"
}
```

## ������ �������:
[����� ���������](https://github.com/VANGAZOR)
[������� ������](https://github.com/Keyreall96)
[�������� ���������](https://github.com/Wests007)
