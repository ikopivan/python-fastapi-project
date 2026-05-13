from app.db.db import SessionLocal
from app.db.crud import get_categories, get_books


session = SessionLocal()

categories = get_categories(session)
books = get_books(session)

print("Категории:\n")

for category in categories:
    print(f"{category.id}. {category.title}")

print("\nКниги:\n")

for book in books:
    print(f"""
ID: {book.id}
Название: {book.title}
Описание: {book.description}
Цена: {book.price}
Категория ID: {book.category_id}
""")