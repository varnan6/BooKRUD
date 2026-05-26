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

---

## 🚀 Free Hosting on Render.com

### Step-by-step

1. **Push your code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/varnan6/BooKRUD.git
   git push -u origin main
   ```

2. **Sign up at [render.com](https://render.com)** (free tier, no credit card needed)

3. **New → Blueprint** → connect your GitHub repo  
   Render auto-detects `render.yaml` and provisions:
   - A **Web Service** running your FastAPI app
   - A **PostgreSQL database** (free tier: 1 GB, 90-day retention)
   - `DATABASE_URL` is wired automatically

4. Click **Deploy** — done! Your API will be live at:  
   `https://bookrud.onrender.com`

### Free tier notes
- The web service **spins down after 15 min of inactivity** (cold start ~30s)
- The free PostgreSQL instance expires after **90 days** (just recreate it)
- For always-on free hosting, see **Railway** or **Fly.io** alternatives below

### Alternative free platforms

| Platform   | Free DB?      | Notes                              |
|------------|---------------|------------------------------------|
| Render.com | ✅ PostgreSQL | Easiest; render.yaml included      |
| Railway    | ✅ PostgreSQL | $5 free credit/month, no sleep     |
| Fly.io     | ✅ PostgreSQL | More control, requires CLI setup   |
| Supabase   | ✅ PostgreSQL | DB only; pair with Render for API  |
