# 🛒 Django-магазин

Bнтернет-магазин на Django с Bootstrap, главной страницей, контактами и формой обратной связи.

---

## 📁 Структура проекта
```
django_shop/
├── catalog/ # Приложение магазина
│ ├── templates/ # HTML-шаблоны
│ │ ├── index.html
│ │ └── contacts.html
│ ├── views.py # Контроллеры
│ ├── urls.py # Маршруты приложения
│ └── ...
├── config/ # Настройки проекта
├── manage.py
├── pyproject.toml
├── poetry.lock
└── README.md
```

## 🚀 Установка и запуск

```bash
# Клонировать репозиторий
git clone https://github.com/LOLIQUR/django_shop.git
cd django_shop

# Установить зависимости
poetry install

# Активировать виртуальное окружение
poetry shell

# Применить миграции
python manage.py migrate

# Запустить сервер
python manage.py runserver
Открыть в браузере: http://127.0.0.1:8000
```

### 📬 Форма обратной связи
```
На странице контакты есть форма:
Имя
Email
Сообщение
После отправки данные выводятся в консоль сервера, 
а пользователь видит сообщение об успехе.
```

### 🛠 Технологии
```
Django
Bootstrap 5
Font Awesome
Python 3.13+
Poetry
```

### 👨‍💻 Автор
Данил Семенов