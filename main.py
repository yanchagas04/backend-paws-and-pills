from fastapi import FastAPI
from src.services.external.dogs_api import get_dog_breeds
from src.services.external.cats_api import get_cat_breeds
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
