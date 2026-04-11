from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL untuk SQLite database.
SQLALCHEMY_DATABASE_URL = "sqlite:///./rental_kamera.db"

# jembatan komunikasi antara aplikasi dan database
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal : sesi koneksi ke database setiap kali ada request
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base : class dasar yang akan diwarisi oleh model tabel 
Base = declarative_base()

# Fungsi dependency untuk mendapatkan session database di FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()