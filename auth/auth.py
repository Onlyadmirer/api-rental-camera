from passlib.context import CryptContext

# algoritma bcrypt untuk mengacak password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    """Fungsi untuk mengacak password asli menjadi hash"""
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    """Fungsi untuk mengecek apakah password yang diinput cocok dengan hash di database"""
    return pwd_context.verify(plain_password, hashed_password)