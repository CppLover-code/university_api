🇷🇺 Русская версия
University API

Учебный backend-проект на Django REST Framework для управления студентами, преподавателями и учебными предметами.

Возможности проекта:
- Аутентификация и авторизация
- JWT Authentication
- Access и Refresh токены
- Ролевая модель доступа (RBAC)

Роли пользователей:

* Admin
* Teacher
* Student
* Работа с данными
* CRUD для студентов
* CRUD для преподавателей
* CRUD для учебных предметов
* PostgreSQL в качестве основной базы данных
* Фильтрация и поиск
* SearchFilter
* OrderingFilter
* DjangoFilterBackend

Примеры:

Поиск студентов:
GET /api/students/?search=student1

Сортировка:
GET /api/students/?ordering=-id

Фильтрация по предмету:
GET /api/students/?subjects=1

Пагинация
Поддерживается постраничная выдача данных через DRF Pagination.

Кэширование
Используется Redis для кэширования ответов API.

Celery и фоновые задачи
Используется Celery + Redis для выполнения фоновых задач.

Реализован сценарий:

Создание студента
→ Django Signal
→ Celery Task
→ Отправка приветственного Email

Email уведомления
Используется SMTP (Gmail).
После создания нового студента автоматически отправляется приветственное письмо.

Документация API

Swagger UI:

http://127.0.0.1:8001/swagger/

Технологии:

Python 3
Django
Django REST Framework
PostgreSQL
Redis
Celery
Docker
Docker Compose
JWT
drf-spectacular (Swagger/OpenAPI)

Запуск проекта:
Клонирование репозитория
git clone <repository_url>
cd university_api

Создание .env
Пример:

SECRET_KEY=your_secret_key

DEBUG=True

DB_NAME=university_db
DB_USER=postgres
DB_PASSWORD=postgres_password
DB_HOST=db
DB_PORT=5432

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
EMAIL_USE_TLS=True

Запуск через Docker
docker compose up --build

Применение миграций
docker compose exec web python manage.py migrate

Создание суперпользователя
docker compose exec web python manage.py createsuperuser

Архитектура:

Browser
↓
Django REST API
↓
PostgreSQL

Django
↓
Redis
↓
Celery Worker
↓
Email Service (SMTP)

Учебные темы, реализованные в проекте:
Django ORM
Custom User Model
JWT Authentication
RBAC
Docker
PostgreSQL
Redis Cache
Celery
Signals
Swagger
Search
Ordering
Filtering
Pagination
Email Notifications

----------------------------------------------------------------
🇬🇧 English Version
University API

Educational backend project built with Django REST Framework for managing students, teachers, and academic subjects.

Features:
- Authentication and Authorization
- JWT Authentication
- Access and Refresh tokens
- Role-Based Access Control (RBAC)

User roles:
* Admin
* Teacher
* Student
* Data Management
* Student CRUD
* Teacher CRUD
* Subject CRUD
* PostgreSQL database
* Search and Filtering
* SearchFilter
* OrderingFilter
* DjangoFilterBackend

Examples:

Search students:
GET /api/students/?search=student1

Ordering:
GET /api/students/?ordering=-id

Filter by subject:
GET /api/students/?subjects=1

Pagination
Pagination is implemented using Django REST Framework.

Caching
Redis is used for API response caching.

Celery Background Tasks
Celery + Redis are used for asynchronous task processing.

Implemented workflow:
Student Creation
→ Django Signal
→ Celery Task
→ Welcome Email

Email Notifications
SMTP (Gmail) integration.
A welcome email is automatically sent after a new student is created.

API Documentation

Swagger UI:
http://127.0.0.1:8001/swagger/

Tech Stack:
Python 3
Django
Django REST Framework
PostgreSQL
Redis
Celery
Docker
Docker Compose
JWT
drf-spectacular (Swagger/OpenAPI)

Installation:

Clone repository
git clone <repository_url>
cd university_api
Create .env file

Example:

SECRET_KEY=your_secret_key

DEBUG=True

DB_NAME=university_db
DB_USER=postgres
DB_PASSWORD=postgres_password
DB_HOST=db
DB_PORT=5432

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
EMAIL_USE_TLS=True

Run with Docker
docker compose up --build

Apply migrations
docker compose exec web python manage.py migrate

Create superuser
docker compose exec web python manage.py createsuperuser

Architecture:
Browser
↓
Django REST API
↓
PostgreSQL

Django
↓
Redis
↓
Celery Worker
↓
Email Service (SMTP)

Topics Covered:
Django ORM
Custom User Model
JWT Authentication
RBAC
Docker
PostgreSQL
Redis Cache
Celery
Signals
Swagger
Search
Ordering
Filtering
Pagination
Email Notifications