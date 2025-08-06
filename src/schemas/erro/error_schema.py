from pydantic import BaseModel

class ErrorSchema(BaseModel):
    status: str
    message: str