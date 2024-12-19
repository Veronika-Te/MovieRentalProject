from pydantic import BaseModel,Field
from . import User_model

class RentalModel(BaseModel):
    user: User_model = Field(default=None)
    movie: str = Field(min_length=1, max_length=20)
    rental_duration: float=Field(gt=0)