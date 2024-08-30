# Проект notes_service

## Описание
`notes_service` - это REST API сервис для создания и управления заметками. Проект реализован на Python с использованием FastAPI, и включает аутентификацию, а также проверку орфографии с помощью Яндекс.Спеллер.

## Технологии
- **FastAPI** - современный веб-фреймворк для создания API на Python.
- **PostgreSQL** - реляционная база данных для хранения заметок.
- **YAPF** (Yet Another Python Formatter) - инструмент для форматирования кода.
- **Git Hooks** - скрипты, которые запускаются на определённых стадиях работы с Git.
- **Яндекс.Спеллер** - сервис для проверки орфографии.

## Установка и запуск

### Клонирование репозитория
```bash
git clone https://github.com/AlexGriv/notes_service.git
cd notes_service


docker-compose up --build
docker-compose down
docker-compose run fastapi alembic revision --autogenerate -m "Initial migration"
docker-compose run fastapi alembic upgrade head
docker-compose up --build

Доступ к API
После запуска зайдите на http://localhost:8000/docs#/, чтобы ознакомиться с документацией API.

Примеры использования API
Регистрация пользователя
POST /auth/register

Получение токена
POST /auth/jwt/login

Создание заметки
POST /new_note/ Заметка проверяется и исправляется с помощью сервиса Яндекс.Спеллер.

Получение списка заметок
GET /all/ Возвращает список заметок пользователя. Суперпользователь видит заметки всех пользователей.

```

### Автор
AlexGriv https://github.com/AlexGriv
