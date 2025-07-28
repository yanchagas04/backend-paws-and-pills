from pydantic import BaseModel

class AnimalSchema(BaseModel):
    id: str
    name: str
    weight: float
    birthday: str
    breed: str
    image: str | None
    type: str