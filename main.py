from fastapi import FastAPI
from database import engine, Base
from models import user, equipment, rental


# membuat file rental_kamera.db beserta tabelnya
Base.metadata.create_all(bind=engine)

# Inisialisasi aplikasi FastAPI
app = FastAPI(
    title="API Rental Kamera",
    description="Sistem Manajemen Rental Kamera menggunakan FastAPI",
    version="1.0.0"
)

# Endpoint (Root)
@app.get("/")
def read_root():
    return {"message": "Selamat datang di API Rental Kamera!"}