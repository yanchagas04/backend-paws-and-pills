from pydantic import BaseModel

class BreedSchema(BaseModel):
    name: str

class BreedsResponseSchema(BaseModel):
    status: str
    breeds: list[BreedSchema] | None