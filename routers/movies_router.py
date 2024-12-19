from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Annotated
from models import Movies
from sqlalchemy.orm import Session
from database.database import SessionLocal
from fastapi.security import OAuth2PasswordBearer
from auth_utils import verify_jwt_token, hash_password

router=APIRouter()
oauth2_scheme= OAuth2PasswordBearer(tokenUrl="token")


class CreateMovieRequest(BaseModel):
    title :str
    genre: str
    rating: int


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]



@router.get("/movies")
async def retrieve_movies(db: db_dependency):
    movies = db.query(Movies).all() 
    return movies

#authenticated
@router.post("/movies")
async def create_movie(db:db_dependency,create_movie_request:CreateMovieRequest,token:str=Depends(oauth2_scheme)):
     #logged in user
    current_username=verify_jwt_token(token)
    #authenticated current username
    movie_user = db.query(Movies).filter(Movies.username == create_movie_request.user).first()
    create_movie_model = Movies (
        user=movie_user.id,
        title=create_movie_request.title,
        genre=create_movie_request.genre,
        rating=create_movie_request.rating
    )
    db.add(create_movie_model)
    db.commit()

