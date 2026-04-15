from pydantic import BaseModel
from datetime import datetime

class RentalBase(BaseModel):
    equipment_id: int
    start_date: datetime
    end_date: datetime

class RentalCreate(RentalBase):
    user_id: int

class RentalResponse(RentalBase):
    id: int
    user_id: int
    total_price: int
    status: str

    class Config:
        from_attributes = True