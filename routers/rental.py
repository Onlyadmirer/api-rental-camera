from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models.rental import Rental
from models.equipment import Equipment
from models.user import User
from schemas.rental import RentalCreate, RentalResponse

router = APIRouter(
    prefix="/rentals",
    tags=["Rental"]
)

# CREATE: Membuat transaksi penyewaan baru
@router.post("/", response_model=RentalResponse, status_code=status.HTTP_201_CREATED)
def create_rental(rental: RentalCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == rental.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")

    equipment = db.query(Equipment).filter(Equipment.id == rental.equipment_id).first()
    if not equipment:
        raise HTTPException(status_code=404, detail="Peralatan tidak ditemukan")

    # Hitung durasi hari
    delta = rental.end_date - rental.start_date
    days = delta.days
    if days < 1:
        days = 1 # Kminimal sewa adalah 1 hari penuh

    # Hitung total harga otomatis
    calculated_total_price = days * equipment.price_per_day

    new_rental = Rental(
        user_id=rental.user_id,
        equipment_id=rental.equipment_id,
        start_date=rental.start_date,
        end_date=rental.end_date,
        total_price=calculated_total_price,
        status="active"
    )
    
    db.add(new_rental)
    db.commit()
    db.refresh(new_rental)
    return new_rental

# READ: Melihat semua data transaksi
@router.get("/", response_model=List[RentalResponse])
def get_all_rentals(db: Session = Depends(get_db)):
    return db.query(Rental).all()