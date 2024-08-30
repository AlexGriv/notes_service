# Проект notes_service (тестовое задание)
## Задание


## Технологии
Fastapi
PostgreSQL
YAPF (Yet Another Python Formatter)
Git Hooks
Яндекс.Спеллер

Выполните команды:
```


docker-compose up --build
docker-compose run fastapi alembic revision --autogenerate -m "Initial migration"
docker-compose run fastapi alembic upgrade head
docker-compose down
docker-compose up --build

Зайдите на http://localhost:8000/docs#/
Создайте пользователя
POST
auth
/auth/register
Получите токен Bearer например для Postman
/auth/jwt/login

Авторизирйтесь Authorize

POST
/new_note/ Создать сообщение, сообщения проверяются и справляются сервисом Яндекс.Спеллер.

GET
/all/ Получить список своих сообщений (суперпользователь видит сообщения всех пользователей)

```

### Автор
AlexGriv https://github.com/AlexGriv
