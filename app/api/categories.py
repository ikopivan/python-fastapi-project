from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.db import SessionLocal
from app.db import crud
from app import schemas


router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.CategoryResponse])
def read_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)


@router.get("/{category_id}", response_model=schemas.CategoryResponse)
def read_category(category_id: int, db: Session = Depends(get_db)):
    category = crud.get_category_by_id(db, category_id)

    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    return category


@router.post("/", response_model=schemas.CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category.title)


@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    category = crud.delete_category(db, category_id)

    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    return {"message": "Category deleted"}