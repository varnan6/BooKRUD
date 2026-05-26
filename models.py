from sqlalchemy import Column, Integer, String, Float, Boolean, Text, DateTime
from sqlalchemy.sql import func
from database import Base


class Book(Base):
    __tablename__ = "books"

    id            = Column(Integer, primary_key=True, index=True)
    title         = Column(String(255), nullable=False, index=True)
    author        = Column(String(255), nullable=False)
    genre         = Column(String(100), nullable=True)
    description   = Column(Text, nullable=True)
    isbn          = Column(String(20), unique=True, nullable=True)
    published_year= Column(Integer, nullable=True)
    price         = Column(Float, nullable=True)
    available     = Column(Boolean, default=True)
    created_at    = Column(DateTime(timezone=True), server_default=func.now())
    updated_at    = Column(DateTime(timezone=True), onupdate=func.now())
