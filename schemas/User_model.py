
from pydantic import BaseModel,Field,EmailStr
from typing import Optional

class UserModel(BaseModel):
    id: Optional[int] = Field(description="ID is not required for creating a user", default=None) 
    name: str = Field(min_length=1, max_length=20)
    email: EmailStr
    password: str = Field(min_length=6, max_length=30)

   


