from pydantic import BaseModel

class DogBreed(BaseModel):
    name: str

class DogBreedsResponse(BaseModel):
    status: str
    breeds: list[DogBreed] | None