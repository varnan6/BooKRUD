import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Fetch the password and explicitly fail if it is missing
db_password = os.getenv("DATABASE_PASSWORD")
if not db_password:
    raise ValueError("CRITICAL: DATABASE_PASSWORD environment variable is not set.")

# 2. Safely construct the connection URL
DATABASE_URL = f"postgresql://postgres:{db_password}@vlexmdmbsojlcsnqgklt.pooler.supabase.com:5432/postgres"

# 3. Initialize SQLAlchemy components
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
