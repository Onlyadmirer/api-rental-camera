from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from fastapi.security import OAuth2PasswordBearer

# Konfigurasi Password Hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Konfigurasi JWT
SECRET_KEY = "kunci_rahasia_proyek_uts_sangat_aman" # Idealnya ini disimpan di .env
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 # Token akan hangus dalam 30 menit

# FastAPI URL mana yang dipakai untuk login
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Fungsi membuat Token JWT
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    # Menggabungkan data, kunci rahasia, dan algoritma menjadi sebuah token
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt