from pydantic import BaseModel,Field

class MovieModel(BaseModel):
    title:str = Field(min_length=1, max_length=20)
    genre:str = Field(min_lenght=1, max_lenght=30)
    rating: int = Field(gt=0, lt=10)
    






