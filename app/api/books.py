from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.db import SessionLocal
from app.db import crud
from app import schemas


router = APIRouter(
    prefix="/books",
    tags=["Books"]
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.BookResponse])
def read_books(
    category_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    if category_id is not None:
        return crud.get_books_by_category(db, category_id)

    return crud.get_books(db)


@router.get("/{book_id}", response_model=schemas.BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book_by_id(db, book_id)

    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    return book


@router.post(
    "/",
    response_model=schemas.BookResponse,
    status_code=status.HTTP_201_CREATED
)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    category = crud.get_category_by_id(db, book.category_id)

    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    return crud.create_book(
        db,
        book.title,
        book.description,
        book.price,
        book.url,
        book.category_id
    )


@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.delete_book(db, book_id)

    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    return {"message": "Book deleted"}