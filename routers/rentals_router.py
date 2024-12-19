from fastapi import APIRouter, Depends
from pydantic import BaseModel
from models import Rentals, Users
from typing import Annotated
from sqlalchemy.orm import Session
from database.database import SessionLocal
from fastapi.security import OAuth2PasswordBearer
from auth_utils import verify_jwt_token, hash_password

router=APIRouter()
oauth2_scheme= OAuth2PasswordBearer(tokenUrl="token")


class CreateRentalRequest(BaseModel):
    user: str
    movie: str
    rental_duration: float


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/rentals")
async def retrieve_rentals(db:db_dependency, token:str=Depends(oauth2_scheme)):
    #logged in user
    current_username=verify_jwt_token(token)
    user = db.query(Users).filter(Users.username == current_username).first()
    if not user:
        return False #throw exception not found
    current_user_rentals=db.query(Rentals).filter(Rentals.user==user.id)
    return current_user_rentals
    
    

@router.post("/rentals")
async def create_rental_movie(db:db_dependency,create_rental_request:CreateRentalRequest,token:str=Depends(oauth2_scheme)):
    #logged in user
    current_username=verify_jwt_token(token)
    #authenticated current
    rental_user = db.query(Users).filter(Users.username == create_rental_request.user).first()
    
    create_rental_model = Rentals (
        user=rental_user.id,
        movie=create_rental_request.movie,
        rental_duration=create_rental_request.rental_duration
    )

    db.add(create_rental_model)
    db.commit()



 