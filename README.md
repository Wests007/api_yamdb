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
git clone ��� ������ ����� ������������
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

### ���� ��� ���������� ��������� ��� ������ ������!!!
### ������� �������� � API:

- ��������� ����������

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

- �������� ����������

POST /api/v1/posts/

```
{
    "text": "string",
    "image": "string",
    "group": 0
}
```
