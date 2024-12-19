
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Path, Query, Request
import schemas
from typing import List
from starlette import status
import uvicorn
import json
import os 
from schemas import UserModel
from routers import auth_router
from dotenv import load_dotenv
from routers import auth_router, movies_router, rentals_router
from database.database import engine
import models
from config import Config

config = Config()

models.Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app=FastAPI(lifespan=lifespan)
load_dotenv() #loading .env

app.include_router(auth_router.router)
app.include_router(movies_router.router)
app.include_router(rentals_router.router)


@app.get("/", status_code=status.HTTP_200_OK)     
async def home():
    return {"message":"Welcome to project MovieRental"}

     
if __name__=="__main__":
   uvicorn.run("main:app",port=config.PORT, reload=True)