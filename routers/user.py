from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import or_

from database import get_db
from models.user import User
from schemas.user import UserCreate, UserResponse
from auth.auth import get_password_hash
from fastapi.security import OAuth2PasswordRequestForm
from auth.auth import verify_password, create_access_token, oauth2_scheme, SECRET_KEY, ALGORITHM
from jose import JWTError, jwt

router = APIRouter(
    prefix="/users",
    tags=["User"]
)

# Endpoint Register User
@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email sudah terdaftar")
    
    hashed_pwd = get_password_hash(user.password)
    
    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=hashed_pwd
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# ENDPOINT LOGIN
@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user_input = form_data.username 
    
    user = db.query(User).filter(
        or_(
            User.email == user_input,
            User.username == user_input
        )
    ).first()
    
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Username/Email atau password salah")
    
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, 
        detail="Sesi tidak valid atau token kadaluarsa",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
        
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise credentials_exception
    return user

# ENDPOINT TERPROTEKSI (Contoh: Melihat profil sendiri)
@router.get("/me", response_model=UserResponse)
def get_user_profile(current_user: User = Depends(get_current_user)):
    # Jika tidak ada token yang valid, fungsi get_current_user akan otomatis menolak akses.
    # Jika lolos, ia akan mengembalikan data user yang sedang login.
    return current_user