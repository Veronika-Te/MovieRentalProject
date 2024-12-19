from database.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import validates

class Movies(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True, index=True)
    title=Column(String)
    genre=Column(String)
    rating=Column(Integer)

    class Config:
        orm_mode = True

    @validates('rating')
    def validate_rating(self, key, rating):
        min=0
        max=10
        if min<=len(rating)<=max:
           return rating
        raise ValueError("Rating should be between 0 and 10.")
