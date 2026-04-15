from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models.equipment import Equipment
from schemas.equipment import EquipmentCreate, EquipmentResponse

#  router khusus untuk equipment
router = APIRouter(
    prefix="/equipments",
    tags=["Equipment"]
)

# CREATE: Menambahkan alat baru
@router.post("/", response_model=EquipmentResponse, status_code=status.HTTP_201_CREATED)
def create_equipment(equipment: EquipmentCreate, db: Session = Depends(get_db)):
    # Ubah data dari Pydantic schema menjadi SQLAlchemy model
    new_equipment = Equipment(**equipment.model_dump())
    db.add(new_equipment)
    db.commit()
    db.refresh(new_equipment)
    return new_equipment

# READ: Mengambil semua daftar alat
@router.get("/", response_model=List[EquipmentResponse])
def get_all_equipments(db: Session = Depends(get_db)):
    equipments = db.query(Equipment).all()
    return equipments

# READ (by ID): Mengambil detail satu alat berdasarkan ID
@router.get("/{equipment_id}", response_model=EquipmentResponse)
def get_equipment(equipment_id: int, db: Session = Depends(get_db)):
    equipment = db.query(Equipment).filter(Equipment.id == equipment_id).first()
    if not equipment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Alat tidak ditemukan")
    return equipment

# UPDATE: Mengubah data alat
@router.put("/{equipment_id}", response_model=EquipmentResponse)
def update_equipment(equipment_id: int, updated_equipment: EquipmentCreate, db: Session = Depends(get_db)):
    equipment_query = db.query(Equipment).filter(Equipment.id == equipment_id)
    equipment = equipment_query.first()
    
    if not equipment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Alat tidak ditemukan")
    
    # Update data
    equipment_query.update(updated_equipment.model_dump(), synchronize_session=False)
    db.commit()
    return equipment_query.first()

# DELETE: Menghapus alat
@router.delete("/{equipment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_equipment(equipment_id: int, db: Session = Depends(get_db)):
    equipment_query = db.query(Equipment).filter(Equipment.id == equipment_id)
    equipment = equipment_query.first()
    
    if not equipment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Alat tidak ditemukan")
    
    equipment_query.delete(synchronize_session=False)
    db.commit()
    return None