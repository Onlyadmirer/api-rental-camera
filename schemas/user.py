from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr
    is_active: bool = True

# Skema register
class UserCreate(UserBase):
    password: str

# Skema response
class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True # Agar Pydantic bisa membaca data dari SQLAlchemy ORM