from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


# ── Shared base ──────────────────────────────────────────────────────────────
class BookBase(BaseModel):
    title:          str            = Field(..., min_length=1, max_length=255, example="The Pragmatic Programmer")
    author:         str            = Field(..., min_length=1, max_length=255, example="Andrew Hunt")
    genre:          Optional[str]  = Field(None, max_length=100, example="Technology")
    description:    Optional[str]  = Field(None, example="A guide to pragmatic programming practices.")
    isbn:           Optional[str]  = Field(None, max_length=20, example="978-0135957059")
    published_year: Optional[int]  = Field(None, ge=1000, le=2100, example=2019)
    price:          Optional[float]= Field(None, ge=0, example=29.99)
    available:      Optional[bool] = Field(True, example=True)


# ── Create (all required fields must be present) ─────────────────────────────
class BookCreate(BookBase):
    pass


# ── Update (every field is optional for partial PATCH-style updates) ─────────
class BookUpdate(BaseModel):
    title:          Optional[str]  = Field(None, min_length=1, max_length=255)
    author:         Optional[str]  = Field(None, min_length=1, max_length=255)
    genre:          Optional[str]  = None
    description:    Optional[str]  = None
    isbn:           Optional[str]  = None
    published_year: Optional[int]  = Field(None, ge=1000, le=2100)
    price:          Optional[float]= Field(None, ge=0)
    available:      Optional[bool] = None


# ── Response (adds DB-generated fields) ──────────────────────────────────────
class BookResponse(BookBase):
    id:         int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True   # Pydantic v2 (was orm_mode in v1)
