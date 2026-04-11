from fastapi import FastAPI

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