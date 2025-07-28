from pydantic import BaseModel

class MedicineSchema(BaseModel):
    id: str
    name: str
    description: str
    amount: float
    periodic: bool
    periodicity: str | None
    startDate: str
    endDate: str | None