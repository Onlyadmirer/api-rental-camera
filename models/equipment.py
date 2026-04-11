from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Equipment(Base):
    __tablename__ = "equipments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String) # Contoh: Kamera, Lensa, Tripod
    stock = Column(Integer)
    price_per_day = Column(Integer)

    # Relasi One-to-Many ke tabel Rental
    rentals = relationship("Rental", back_populates="equipment")