from sqlalchemy.orm import Session
from models import Book
from schemas import BookCreate, BookUpdate


def create_book(db: Session, book: BookCreate) -> Book:
    """Insert a new book record into the database."""
    db_book = Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_books(db: Session, skip: int = 0, limit: int = 100) -> list[Book]:
    """Return all books with optional pagination."""
    return db.query(Book).offset(skip).limit(limit).all()


def get_book(db: Session, book_id: int) -> Book | None:
    """Return a single book by primary key."""
    return db.query(Book).filter(Book.id == book_id).first()


def update_book(db: Session, book_id: int, book_data: BookUpdate) -> Book | None:
    """Update only the fields that were provided (partial update)."""
    db_book = get_book(db, book_id)
    if not db_book:
        return None

    update_fields = book_data.model_dump(exclude_unset=True)
    for field, value in update_fields.items():
        setattr(db_book, field, value)

    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int) -> bool:
    """Delete a book by ID. Returns True on success, False if not found."""
    db_book = get_book(db, book_id)
    if not db_book:
        return False

    db.delete(db_book)
    db.commit()
    return True
