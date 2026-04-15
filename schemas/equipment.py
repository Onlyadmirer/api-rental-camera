from pydantic import BaseModel

class EquipmentBase(BaseModel):
    name: str
    category: str
    stock: int
    price_per_day: int

class EquipmentCreate(EquipmentBase):
    pass

class EquipmentResponse(EquipmentBase):
    id: int

    class Config:
        from_attributes = True