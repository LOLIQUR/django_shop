# 🛒 Django-магазин

Интернет-магазин на Django с Bootstrap, PostgreSQL, моделями, админкой, фикстурами и кастомными командами.

## 📁 Структура проекта

```
django_shop/
├── catalog/
│   ├── management/commands/
│   ├── migrations/
│   ├── templates/
│   │   ├── index.html
│   │   └── contacts.html
│   ├── models.py
│   ├── admin.py
│   ├── views.py
│   └── urls.py
├── config/
├── fixtures/
├── screenshots/
├── media/
├── .env
├── manage.py
├── pyproject.toml
├── poetry.lock
└── README.md
```

## 🚀 Установка и запуск

```bash
git clone https://github.com/LOLIQUR/django_shop.git
cd django_shop
poetry install
poetry shell
python manage.py migrate
python manage.py runserver
```

Открыть в браузере: http://127.0.0.1:8000

## 🗄️ База данных

```
Проект использует PostgreSQL. Настройки в .env:

DB_NAME=django_shop
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

## 📦 Модели

```
Category: name, description
Product: name, description, price, category, image, created_at, updated_at
```

## 🧪 Кастомная команда

```bash
python manage.py load_data
Очищает таблицы и загружает данные из fixtures/.
```

## 📬 Форма обратной связи

```
На странице /contacts/ есть форма: Имя, Email, Сообщение. После отправки данные выводятся в консоль.
```

## 👨‍💻 Автор
```
Данил Семенов
GitHub: LOLIQUR
```
