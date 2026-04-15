# API Rental Kamera

Sistem Manajemen Rental Kamera yang dibangun dengan **FastAPI**, SQLite, dan JWT Authentication. Aplikasi ini menyediakan API untuk mengelola pengguna, peralatan kamera, dan transaksi rental.

## 📋 Daftar Isi

- [Fitur Utama](#fitur-utama)
- [Teknologi yang Digunakan](#teknologi-yang-digunakan)
- [Persyaratan Sistem](#persyaratan-sistem)
- [Instalasi](#instalasi)
- [Konfigurasi](#konfigurasi)
- [Menjalankan Aplikasi](#menjalankan-aplikasi)
- [Struktur Proyek](#struktur-proyek)
- [API Endpoints](#api-endpoints)
- [Dokumentasi API](#dokumentasi-api)
- [Catatan Pengembang](#catatan-pengembang)

## ✨ Fitur Utama

- **Autentikasi Pengguna**: Sistem login & registrasi dengan JWT
- **Manajemen Pengguna**: CRUD operasi untuk data pengguna
- **Manajemen Peralatan**: Kelola daftar kamera dan peralatan rental
- **Sistem Rental**: Proses peminjaman dan pengembalian peralatan
- **Enkripsi Password**: Menggunakan bcrypt untuk keamanan password
- **Database SQLite**: Penyimpanan data yang ringan dan mudah
- **API Documentation**: Dokumentasi interaktif dengan Swagger UI

## 🛠 Teknologi yang Digunakan

| Teknologi             | Versi    | Keterangan                            |
| --------------------- | -------- | ------------------------------------- |
| **FastAPI**           | Latest   | Web framework modern untuk REST API   |
| **Uvicorn**           | Latest   | ASGI server untuk menjalankan FastAPI |
| **SQLAlchemy**        | Latest   | ORM untuk database operations         |
| **Pydantic**          | Latest   | Validasi data dan serialisasi         |
| **JWT (Python-Jose)** | Latest   | Autentikasi berbasis token            |
| **Bcrypt**            | 4.0.1    | Hashing password yang aman            |
| **SQLite**            | Built-in | Database yang ringan                  |

## 🔧 Persyaratan Sistem

- **Python**: 3.8 atau lebih tinggi
- **pip**: Package manager Python
- **OS**: Windows, macOS, atau Linux

## 📦 Instalasi

### 1. Clone Repository

```bash
git clone <repository-url>
cd rental-camera
```

### 2. Buat Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## ⚙️ Konfigurasi

### File Database

Database akan otomatis dibuat saat aplikasi pertama kali dijalankan dengan nama `rental_kamera.db`.

### JWT Secret Key

Edit file [auth/auth.py](auth/auth.py#L9) dan ubah `SECRET_KEY`:

```python
SECRET_KEY = "kunci_rahasia_proyek_uts_sangat_aman"  # Ubah ke kunci yang lebih aman
```

**⚠️ Catatan**: Untuk production, sebaiknya gunakan environment variable (`.env`).

### Token Expiration

Durasi token dapat diatur di [auth/auth.py](auth/auth.py#L11):

```python
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Ubah sesuai kebutuhan
```

## 🚀 Menjalankan Aplikasi

### Development Mode (dengan Auto Reload)

```bash
uvicorn main:app --reload
```

Aplikasi akan berjalan di `http://localhost:8000`

### Production Mode

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## 📁 Struktur Proyek

```
rental-camera/
├── main.py                 # Entry point aplikasi FastAPI
├── database.py             # Konfigurasi koneksi database SQLite
├── requirements.txt        # Daftar dependensi Python
├── structure.txt           # Dokumentasi struktur proyek
├── rental_kamera.db        # Database SQLite (auto-generated)
│
├── auth/
│   └── auth.py            # JWT & password hashing logic
│
├── models/                # SQLAlchemy ORM Models
│   ├── user.py           # Model untuk pengguna
│   ├── equipment.py      # Model untuk peralatan kamera
│   └── rental.py         # Model untuk transaksi rental
│
├── schemas/              # Pydantic schemas untuk validasi
│   ├── user.py          # Schema input/output pengguna
│   ├── equipment.py     # Schema input/output peralatan
│   └── rental.py        # Schema input/output rental
│
├── routers/             # API route handlers
│   ├── user.py         # Endpoints untuk manajemen pengguna
│   ├── equipment.py    # Endpoints untuk manajemen peralatan
│   └── rental.py       # Endpoints untuk manajemen rental
│
└── README.md            # File dokumentasi ini
```

## 🔌 API Endpoints

### User Management

| Method   | Endpoint           | Deskripsi                           |
| -------- | ------------------ | ----------------------------------- |
| `POST`   | `/users/register`  | Daftar pengguna baru                |
| `POST`   | `/users/login`     | Login pengguna                      |
| `GET`    | `/users/me`        | Dapatkan profil pengguna yang login |
| `GET`    | `/users/`          | Daftar semua pengguna (admin only)  |
| `GET`    | `/users/{user_id}` | Dapatkan detail pengguna            |
| `PUT`    | `/users/{user_id}` | Update data pengguna                |
| `DELETE` | `/users/{user_id}` | Hapus pengguna                      |

### Equipment Management

| Method   | Endpoint                    | Deskripsi              |
| -------- | --------------------------- | ---------------------- |
| `GET`    | `/equipment/`               | Daftar semua peralatan |
| `GET`    | `/equipment/{equipment_id}` | Detail peralatan       |
| `POST`   | `/equipment/`               | Tambah peralatan baru  |
| `PUT`    | `/equipment/{equipment_id}` | Update peralatan       |
| `DELETE` | `/equipment/{equipment_id}` | Hapus peralatan        |

### Rental Management

| Method   | Endpoint              | Deskripsi           |
| -------- | --------------------- | ------------------- |
| `GET`    | `/rental/`            | Daftar semua rental |
| `POST`   | `/rental/`            | Buat rental baru    |
| `GET`    | `/rental/{rental_id}` | Detail rental       |
| `PUT`    | `/rental/{rental_id}` | Update rental       |
| `DELETE` | `/rental/{rental_id}` | Batalkan rental     |

## 📚 Dokumentasi API

Setelah menjalankan aplikasi, akses dokumentasi interaktif:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 💡 Catatan Pengembang

### Database Schema

Database SQLite akan memiliki tabel-tabel berikut:

- **users**: Menyimpan data pengguna dan hash password
- **equipment**: Menyimpan data peralatan kamera
- **rentals**: Menyimpan transaksi rental

### Keamanan

1. **Password Hashing**: Semua password di-hash menggunakan bcrypt
2. **JWT Authentication**: Token JWT dikirim pada setiap request yang memerlukan autentikasi
3. **Token Expiration**: Token akan hangus setelah 30 menit (dapat dikonfigurasi)

### Environment Variables (Rekomendasi untuk Production)

Buat file `.env`:

```
SECRET_KEY=your_secret_key_here
DATABASE_URL=sqlite:///./rental_kamera.db
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Testing API

Gunakan tools seperti:

- **Postman**: GUI-based API testing
- **cURL**: Command-line alternative
- **Thunder Client**: VS Code extension

Contoh request dengan cURL:

```bash
# Register
curl -X POST "http://localhost:8000/users/register" \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"password123"}'

# Login
curl -X POST "http://localhost:8000/users/login" \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"password123"}'

# Get Protected Data
curl -X GET "http://localhost:8000/users/me" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

## 🐛 Troubleshooting

### Error: ModuleNotFoundError

Pastikan virtual environment sudah diaktifkan dan dependencies terinstall:

```bash
pip install -r requirements.txt
```

### Error: Database locked

Jangan menjalankan dua instance aplikasi dengan database yang sama.

### Error: 401 Unauthorized

Pastikan token JWT valid dan belum expired. Login ulang untuk mendapatkan token baru.

## 📝 License

Proyek ini dibuat untuk keperluan Proyek UTS WEB (Semester 4).

## ✍️ Author

Dibuat dengan ❤️ untuk mata kuliah Proyek UTS WEB

---

**Terakhir diupdate**: April 2026
