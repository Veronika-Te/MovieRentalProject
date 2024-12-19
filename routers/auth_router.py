from fastapi import APIRouter,Depends
from pydantic import BaseModel
from database.database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from auth_utils import create_jwt_token, verify_jwt_token, hash_password, verify_password
from starlette import status
from models import Users
from passlib.context import CryptContext
router=APIRouter()

# Create a password hashing context using bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class CreateUserRequest(BaseModel):
    username: str
    email: str
    password: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]



@router.post("/auth/register", status_code=status.HTTP_201_CREATED)
async def register_user(db: db_dependency,
                      create_user_request: CreateUserRequest):
    create_user_model = Users (
        email=create_user_request.email,
        username=create_user_request.username,
        hashed_password=hash_password(create_user_request.password)
    )

    db.add(create_user_model)
    db.commit()


@router.post("/auth/login")
async def login_user(db: db_dependency,
                      create_user_request: CreateUserRequest):
    user = db.query(Users).filter(Users.username ==create_user_request.username).first()
    if not user:
        return False
    if not verify_password(create_user_request.password, user.hashed_password):
        return False
    token=create_jwt_token(user.username)
    return {"token":f"{token}"}






    







