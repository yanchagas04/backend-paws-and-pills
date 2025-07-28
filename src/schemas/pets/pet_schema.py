from pydantic import BaseModel

class PetSchema(BaseModel):
    id: str
    name: str
    weight: float
    birthday: str
    breed: str
    image: str | None
    type: str

class PetListResponseSchema(BaseModel):
    status: str
    Pets: list[PetSchema]

class PetResponseSchema(BaseModel):
    status: str
    Pet: PetSchema