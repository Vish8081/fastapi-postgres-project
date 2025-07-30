from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pathlib import Path
import os

# Load .env from project root (explicit path)
env_path = Path('.') / '.env'
if env_path.exists():
    from dotenv import load_dotenv
    load_dotenv(env_path)

# Fallback connection string if .env fails
DEFAULT_DB_URL = "postgresql://postgres:admin@localhost:5432/postgres"
SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL", DEFAULT_DB_URL)

# Verify the URL is set
if not SQLALCHEMY_DATABASE_URL:
    raise ValueError("No database URL configured!")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()