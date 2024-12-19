from database.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import validates
import re


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
   
    class Config:
        orm_mode = True

    @validates('email')
    def validate_email(self, key, value):
        # Regex for validating email format
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, value):
            raise ValueError(f"Invalid email format: {value}")
        return value