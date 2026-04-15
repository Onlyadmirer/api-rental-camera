from fastapi import FastAPI
from database import engine, Base
from models import user, equipment, rental

from routers import equipment, user, rental


# membuat file rental_kamera.db beserta tabelnya
Base.metadata.create_all(bind=engine)

# Inisialisasi aplikasi FastAPI
app = FastAPI(
    title="API Rental Kamera",
    description="Sistem Manajemen Rental Kamera menggunakan FastAPI",
    version="1.0.0"
)

app.include_router(equipment.router)
app.include_router(user.router)
app.include_router(rental.router)

# Endpoint (Root)
@app.get("/")
def read_root():
    return {"message": "Selamat datang di API Rental Kamera!"}