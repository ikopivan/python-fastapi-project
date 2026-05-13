from app.db.models import Category, Book


# CATEGORY CRUD

def create_category(session, title):
    category = Category(title=title)

    session.add(category)
    session.commit()
    session.refresh(category)

    return category


def get_categories(session):
    return session.query(Category).all()


def get_category_by_id(session, category_id):
    return session.query(Category).filter(Category.id == category_id).first()


def delete_category(session, category_id):
    category = get_category_by_id(session, category_id)

    if category:
        session.delete(category)
        session.commit()

    return category


# BOOK CRUD

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


def get_books(session):
    return session.query(Book).all()


def get_book_by_id(session, book_id):
    return session.query(Book).filter(Book.id == book_id).first()


def get_books_by_category(session, category_id):
    return session.query(Book).filter(Book.category_id == category_id).all()


def delete_book(session, book_id):
    book = get_book_by_id(session, book_id)

    if book:
        session.delete(book)
        session.commit()

    return book