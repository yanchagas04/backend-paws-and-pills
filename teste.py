from fastapi import FastAPI
from src.schemas.user.user_schema import UserSchema
from src.services.user.user_service import UserService
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/user")
async def get_user_route():
    user_id = "1"
    return await UserService().get_user(user_id)

@app.post("/user")
async def create_user_route():
    user = UserSchema(id="1", name="test", email="test", password="test", image="test")
    return await UserService().create_user(user)

@app.put("/user/{user_id}")
async def update_user_route(user_id: str):
    user = UserSchema(id="1", name="testando", email="test", password="test", image="test")
    return await UserService().update_user(user_id, user)

@app.delete("/user/{user_id}")
async def delete_user_route():
    user_id = "1"
    return await UserService().delete_user(user_id)