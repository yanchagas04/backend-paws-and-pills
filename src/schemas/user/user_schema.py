from pydantic import BaseModel

class UserSchema(BaseModel):
    id: str
    name: str
    email: str
    password: str
    image: str

class UserResponseSchema(BaseModel):
    status: str
    user: UserSchema