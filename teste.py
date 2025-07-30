from fastapi import FastAPI
from src.schemas.user.user_schema import UserSchema
from src.services.user.user_service import UserService
from typing import Annotated, Required
from fastapi import Query, Path
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/user")
async def get_user_route(
    user_id: Annotated[str, Query(alias="user_id", description="ID do usuário")]
):
    return await UserService().get_user(user_id)

@app.get("/users")
async def get_users_route():
    return await UserService().get_users()

@app.post("/user")
async def create_user_route(
    name: Annotated[str, Query(alias="name", description="Nome do usuário")],
    email: Annotated[str, Query(alias="email", description="Email do usuário")],
    password: Annotated[str, Query(alias="password", description="Senha do usuário")]
):
    user = UserSchema(name=name, email=email, password=password, image="test")
    return await UserService().create_user(user)

@app.put("/user/{user_id}")
async def update_user_route(
    user_id: Annotated[str, Path(alias="user_id", description="ID do usuário")],
    name: Annotated[str, Query(alias="name", description="Nome do usuário")],
    email: Annotated[str, Query(alias="email", description="Email do usuário")],
    password: Annotated[str, Query(alias="password", description="Senha do usuário")]
):
    user = UserSchema(name=name, email=email, password=password, image="test")
    return await UserService().update_user(user_id, user)

@app.delete("/user")
async def delete_user_route(
    user_id: Annotated[str, Query(alias="user_id", description="ID do usuário")]
):
    return await UserService().delete_user(user_id)