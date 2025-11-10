from pydantic import BaseModel, Field, ConfigDict

class DogBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=10)
    age: int = Field(..., ge=0)

class DogCreate(DogBase):
    pass

class DogResponse(DogBase):
    id: int
    model_config = ConfigDict(from_attributes=True)