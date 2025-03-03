# Древовидная структура отделов

## Описание

Это веб-приложение на Django, которое отображает древовидную структуру отделов с возможностью просмотра сотрудников. Приложение позволяет управлять записями через административную панель Django и поддерживает иерархию отделов до 5 уровней.

## Функциональные возможности

- Отображение главных отделов и их подотделов.
- Просмотр сотрудников, связанных с каждым отделом и подотделом.
- Управление записями сотрудников и отделов через административную панель Django.

## Технологии

- Python 3.10+
- Django 3+
- SQLite
- Bootstrap 4 для стилизации

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/Dm-Str/OrgChart.git
   cd ваш_репозиторий

2. Создайте виртуальное окружение и активируйте его:
   ```bash
   python3.10 -m venv venv
   source venv/bin/activate  # Для Linux/Mac
   venv\Scripts\activate  # Для Windows

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt

4. Выполните миграции:
   ```bash
   python manage.py migrate

5. Создайте суперпользователя для доступа к административной панели:
   ```bash
   python manage.py createsuperuser

6. Заполните базу данных тестовыми данными:
   ```bash
    python manage.py create_sample_data

7. Запустите сервер:
   ```bash
   python manage.py runserver
   
14. Перейдите в браузере по адресу http://127.0.0.1:8000/ для просмотра структуры или http://localhost:8000/admin/ для управления записями.
