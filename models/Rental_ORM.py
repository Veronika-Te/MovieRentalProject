from database.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey,Float

class Rentals(Base):
    __tablename__="rentals"
    id = Column(Integer, primary_key=True, index=True)
    user=Column(Integer, ForeignKey('users.id'), nullable=False) #id
    movie=Column(String)
    rental_duration=Column(Float)

    
    class Config:
        orm_mode = True

 