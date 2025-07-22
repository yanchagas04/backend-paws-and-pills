from fastapi import FastAPI
from src.services.external.dogs_api import get_dogs_breeds
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/breeds")
async def get_breeds():
    return await get_dogs_breeds()