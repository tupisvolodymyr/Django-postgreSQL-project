Cinema Project (Django ORM + PostgreSQL)

Навчальний проект для відпрацювання навичок роботи з Django ORM та базою даних PostgreSQL.

Технічні характеристики

Python: 3.14

Django: 5.0+

База даних: PostgreSQL

Основні бібліотеки: psycopg2-binary, python-dotenv

Опис моделей:
Проект містить наступні сутності:

Genre: Назва жанру (Drama, Sci-Fi тощо).

Director: Інформація про режисера (ім'я, прізвище, країна).

Movie: Основна інформація про фільм (назва, рік, рейтинг, тривалість).

Review: Користувацькі відгуки з оцінкою.

Як запустити проект:
Клонуйте репозиторій.
Встановіть залежності:

pip install django psycopg2-binary python-dotenv


Налаштуйте середовище:
Створіть файл .env у корені проекту та додайте ваші дані PostgreSQL:

DB_NAME=cinema_db
DB_USER=postgres
DB_PASSWORD=ваш_пароль
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=ваш_ключ_з_settings


Запустіть міграції:

python manage.py migrate


Запуск запитів:
Виконайте файл зі сценаріями:

python queries.py
