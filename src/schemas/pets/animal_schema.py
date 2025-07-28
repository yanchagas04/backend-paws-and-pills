from pydantic import BaseModel

class AnimalSchema(BaseModel):
    id: str
    name: str
    weight: float
    birthday: str
    breed: str
    image: str | None
    type: str

class AnimalListResponseSchema(BaseModel):
    status: str
    animals: list[AnimalSchema]

class AnimalResponseSchema(BaseModel):
    status: str
    animal: AnimalSchema