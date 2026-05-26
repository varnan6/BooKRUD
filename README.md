# 📚 BooKRUD: A Library Management System

A production-ready REST API for managing a library's book catalog.

---

## Project Structure

```
bookrud/
├── main.py          # FastAPI app & route definitions
├── database.py      # SQLAlchemy engine & session setup
├── models.py        # ORM model (Book table)
├── schemas.py       # Pydantic request/response schemas
├── crud.py          # Database CRUD operations
├── requirements.txt
├── render.yaml      # One-click Render.com deployment
└── .env.example
```

---

## API Endpoints

| Method | Endpoint         | Description              |
|--------|-----------------|--------------------------|
| GET    | `/`             | Health check / welcome   |
| POST   | `/books/`       | Add a new book           |
| GET    | `/books/`       | Get all books            |
| GET    | `/books/{id}`   | Get a book by ID         |
| PUT    | `/books/{id}`   | Update a book by ID      |
| DELETE | `/books/{id}`   | Delete a book by ID      |

Interactive docs available at `/docs` (Swagger UI) and `/redoc`.

---

## Local Setup

### 1. Prerequisites
- Python 3.11+
- PostgreSQL running locally

### 2. Create the database
```sql
CREATE DATABASE bookrud_db;
```

### 3. Clone & install dependencies
```bash
git clone https://github.com/varnan6/BooKRUD
cd bookrud
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Configure environment
```bash
cp .env.example .env
# Edit .env and set your DATABASE_URL
```

### 5. Run the server
```bash
uvicorn main:app --reload
```

Visit: http://localhost:8000/docs

---

## Example Requests

### Add a book
```bash
curl -X POST http://localhost:8000/books/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Clean Code",
    "author": "Robert C. Martin",
    "genre": "Technology",
    "isbn": "978-0132350884",
    "published_year": 2008,
    "price": 35.99,
    "available": true
  }'
```

### Get all books
```bash
curl http://localhost:8000/books/
```

### Get book by ID
```bash
curl http://localhost:8000/books/1
```

### Update a book (partial update supported)
```bash
curl -X PUT http://localhost:8000/books/1 \
  -H "Content-Type: application/json" \
  -d '{"price": 29.99, "available": false}'
```

### Delete a book
```bash
curl -X DELETE http://localhost:8000/books/1
```
