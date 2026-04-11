from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
import datetime

class Rental(Base):
    __tablename__ = "rentals"

    id = Column(Integer, primary_key=True, index=True)
    # Foreign key yang menghubungkan ke tabel user dan equipment
    user_id = Column(Integer, ForeignKey("users.id"))
    equipment_id = Column(Integer, ForeignKey("equipments.id"))
    
    start_date = Column(DateTime, default=datetime.datetime.utcnow)
    end_date = Column(DateTime)
    total_price = Column(Integer)
    status = Column(String, default="pending") # Status: pending, active, returned

    # Relasi balik untuk menarik data User dan Equipment dari data Rental
    user = relationship("User", back_populates="rentals")
    equipment = relationship("Equipment", back_populates="rentals")