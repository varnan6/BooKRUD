import logging
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal, engine, Base
import models
import schemas
import crud

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Library Management System",
    description="A backend REST API to manage books using FastAPI & PostgreSQL",
    version="1.0.0"
)


@app.on_event("startup")
def startup():
    logger.info("Starting up — attempting DB connection...")
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("✅ Database tables created successfully.")
    except Exception as e:
        logger.error(f"❌ Database connection failed: {e}")
        raise e


# Dependency: get DB session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", tags=["Root"])
def root():
    return {"message": "Welcome to the Library Management System API"}


# ─── CREATE ───────────────────────────────────────────────────────────────────

@app.post("/books/", response_model=schemas.BookResponse, status_code=201, tags=["Books"])
def add_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    """Add a new book to the library."""
    return crud.create_book(db, book)


# ─── READ ALL ─────────────────────────────────────────────────────────────────

@app.get("/books/", response_model=List[schemas.BookResponse], tags=["Books"])
def get_all_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Retrieve all books. Supports pagination via skip & limit."""
    return crud.get_books(db, skip=skip, limit=limit)


# ─── READ ONE ─────────────────────────────────────────────────────────────────

@app.get("/books/{book_id}", response_model=schemas.BookResponse, tags=["Books"])
def get_book(book_id: int, db: Session = Depends(get_db)):
    """Retrieve a single book by its ID."""
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail=f"Book with ID {book_id} not found")
    return book


# ─── UPDATE ───────────────────────────────────────────────────────────────────

@app.put("/books/{book_id}", response_model=schemas.BookResponse, tags=["Books"])
def update_book(book_id: int, book_data: schemas.BookUpdate, db: Session = Depends(get_db)):
    """Update an existing book by ID (partial updates supported)."""
    updated = crud.update_book(db, book_id, book_data)
    if not updated:
        raise HTTPException(status_code=404, detail=f"Book with ID {book_id} not found")
    return updated


# ─── DELETE ───────────────────────────────────────────────────────────────────

@app.delete("/books/{book_id}", tags=["Books"])
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """Delete a book by its ID."""
    deleted = crud.delete_book(db, book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"Book with ID {book_id} not found")
    return {"message": f"Book with ID {book_id} has been deleted successfully"}