# Blogs service  RESTful-API

[Задание](https://drive.google.com/file/d/1bWf5agckf8XK6Jg-y3OUXbVifEUmsYvF/view)

RESTful-API бэкенд для сервиса блогов

## Стэк
* Python 3.10
* Django + DRF 4.2.4
* Swagger (drf-yasg) 1.21.7
* PostgreSQL 15.2

## Запуск

### Clone repo
```git clone git@github.com:Cream-Crusher/blogs-rest-api.git```
### Install dependencies
A. Linux:
  1. ```pip install -r requirements.txt```

B. Windows:
  1. Replace ```psycopg2-binary==2.9.7``` with ```psycopg2==2.9.7``` in **requirements.txt**
  2. ```pip install -r requirements.txt```

### Connect PostgreSQL database
1. Create new database ```%db_name%```
2. Edit **db_connect.py**:
```
dbname = '%db_name%'
user = 'username'
password = 'password'
host = 'localhost' # default: localhost
```

### Apply migrations
```python3 manage.py migrate```

### Run server
```python3 manage.py runserver```

### View Swagger
```http://localhost:8000/swagger/#```

## Особенности реализации
### Сущностные классы (поддерживают CRUD):
* User (extends Django User)
* Blog
* Post
* Comment
* Tag

### Функционал:
#### Блоги
* Фильтры и сортировка: **title**, **owner**, **authors**, **created_at**, **updated_at**;
* Подписка: пользователь может добавлять блог в свои подписки при  редактировании профиля *PUT*-запросом ```/user/{id}/```;
* Пагинация: при получении списка блогов выводятся **10** записей на страницу.

#### Посты 
* Фильтры и сортировка: **title**, **author**, **created_at**, **updated_at**, **tags**, **like_count**, **relevance**;
* Лайки: пользователь могут ставить и убирать лайки постам, через *api* ```/post/{id}/like/``` (ограничение для 1  пользователя). С редиректом на ```/post/{id}/```;
* Просмотры: каждый *GET*-запрос ```/post/{id}/``` от аутентифицированного пользователя увеличивает счетчик просмотров запрошенного поста (без ограничений для 1 пользователя);
* Пагинация: при получении списка постов выводятся **10** записей на страницу.

## Оптимизации
1. Подключен **debug-toolbar** для профилирования запросов.
2. Повторные запросы к БД оптимизированны через **lazy_serializer**, **prefetch_related**, **select_related**, **annotate**. Эффект проявится на большой БД.