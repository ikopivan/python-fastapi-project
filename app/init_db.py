from app.db.db import Base, engine, SessionLocal
from app.db.crud import create_category, create_book

from app.db.models import Category, Book

# Создание таблиц
Base.metadata.create_all(bind=engine)

session = SessionLocal()

# Категории
fiction = create_category(session, "Фантастика")
programming = create_category(session, "Программирование")

# Книги
create_book(
    session,
    "Dune",
    "Фантастический роман",
    29.99,
    "",
    fiction.id
)

create_book(
    session,
    "Neuromancer",
    "Киберпанк роман",
    24.99,
    "",
    fiction.id
)

create_book(
    session,
    "Learning Python",
    "Книга по Python",
    39.99,
    "",
    programming.id
)

create_book(
    session,
    "Fluent Python",
    "Продвинутый Python",
    44.99,
    "",
    programming.id
)

print("База данных заполнена!")