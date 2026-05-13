from app.db.models import Category, Book


# CREATE CATEGORY
def create_category(session, title):
    category = Category(title=title)

    session.add(category)
    session.commit()
    session.refresh(category)

    return category


# GET ALL CATEGORIES
def get_categories(session):
    return session.query(Category).all()


# CREATE BOOK
def create_book(session, title, description, price, url, category_id):
    book = Book(
        title=title,
        description=description,
        price=price,
        url=url,
        category_id=category_id
    )

    session.add(book)
    session.commit()
    session.refresh(book)

    return book


# GET ALL BOOKS
def get_books(session):
    return session.query(Book).all()