# Cinema Django Project 🎬

Навчальний проект на Django для керування базою даних фільмів, жанрів та режисерів. Проект демонструє роботу з Django ORM та інтеграцію з PostgreSQL.

## 🚀 Як запустити проект локально

Дотримуйтесь цих кроків, щоб налаштувати проект на своєму комп'ютері.

### 1. Клонування репозиторію
```bash
https://github.com/tupisvolodymyr/Django-postgreSQL-project.git
```

 
 ### 2. Створення та активація віртуального середовища
```bash
python -m venv .venv
# Для Windows:
.venv\Scripts\activate
# Для macOS/Linux:
source .venv/bin/activate
```

### 3. Встановлення залежностей
```Bash
pip install -r requirements.txt
```

_Якщо файлу requirements.txt немає, встановіть вручну: pip install django psycopg2-binary python-dotenv)_

### 4. Налаштування змінних оточення (.env)

```bash
Створіть файл .env у корені проекту (поруч із manage.py) та додайте туди ваші дані:

Фрагмент коду
SECRET_KEY=ваш_секретний_ключ
DEBUG=True

DB_NAME=cinema_db
DB_USER=postgres
DB_PASSWORD=ваш_пароль_від_postgres
DB_HOST=localhost
DB_PORT=5432
```

### 5. Запуск міграцій та бази даних
Переконайтеся, що PostgreSQL запущено і база даних cinema_db створена. Виконайте команди:
```Bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Запуск сервера
```Bash
python manage.py runserver
```

# 🛠 Технології
 _Python 3.14_

 _Django 6.0.3_

 _PostgreSQL_

_python-dotenv (для безпечного зберігання паролів)_

# 📂 Опис моделей
_Genre — жанри фільмів із сортуванням за назвою._

_Director — інформація про режисерів (ім'я, країна, рік народження)._

_Movie — дані про фільм (рейтинг, тривалість, зв'язок з режисером)._

_Review — відгуки користувачів з валідацією оцінки від 1 до 10._
