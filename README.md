# Books API

Проект на Python с использованием FastAPI, SQLAlchemy и PostgreSQL.

## Возможности API

- Получение списка книг
- Получение книги по ID
- Создание книги
- Удаление книги
- Получение списка категорий
- Получение категории по ID
- Создание категории
- Удаление категории
- Фильтрация книг по категории

## Стек технологий

- Python
- FastAPI
- Uvicorn
- PostgreSQL
- SQLAlchemy
- python-dotenv

## Структура проекта

```text
app/
│
├── api/
│   ├── books.py
│   └── categories.py
│
├── db/
│   ├── crud.py
│   ├── db.py
│   └── models.py
│
├── schemas.py
├── init_db.py
└── main.py
```

## Установка зависимостей

```bash
source venv/bin/activate
pip install -r requirements.txt
```

## Настройка базы данных

Создайте файл `.env`:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=octagon_db
DB_USER=octagon
DB_PASSWORD=12345
```

## Инициализация базы данных

```bash
python3 -m app.init_db
```

## Запуск API

```bash
python3 -m uvicorn app.main:app --reload
```

## Swagger документация

```text
http://127.0.0.1:8000/docs
```

## Скриншоты

Скриншоты работы API находятся в папке `examples/`.
