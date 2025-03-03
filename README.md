# Древовидная структура отделов

## Описание

Это веб-приложение на Django, которое отображает древовидную структуру отделов с возможностью просмотра сотрудников. Приложение позволяет управлять записями через административную панель Django и поддерживает иерархию отделов до 5 уровней.

## Функциональные возможности

- Отображение главных отделов и их подотделов.
- Просмотр сотрудников, связанных с каждым отделом и подотделом.
- Управление записями сотрудников и отделов через административную панель Django.
- Оптимизация загрузки данных с использованием `prefetch_related` и кэширования.

## Технологии

- Python 3.9+
- Django 3+
- SQLite
- Bootstrap 4 для стилизации

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/ваш_логин/ваш_репозиторий.git
   cd ваш_репозиторий

2. Создайте виртуальное окружение и активируйте его:
   python -m venv venv
   source venv/bin/activate  # Для Linux/Mac
   venv\Scripts\activate  # Для Windows

3. Установите зависимости:
   pip install -r requirements.txt

4. Выполните миграции:
   python manage.py migrate

5. Создайте суперпользователя для доступа к административной панели:
   python manage.py createsuperuser

6. Заполните базу данных тестовыми данными:
   python manage.py create_sample_data

7. Запустите сервер:
   python manage.py runserver
   
8. Перейдите в браузере по адресу http://127.0.0.1:8000/
