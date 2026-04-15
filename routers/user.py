from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from models.user import User
from schemas.user import UserCreate, UserResponse
from auth.auth import get_password_hash

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