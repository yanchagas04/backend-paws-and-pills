from pydantic import BaseModel

class MedicineSchema(BaseModel):
    id: str | None
    name: str
    description: str
    amount: float
    periodic: bool
    periodicity: str | None
    startDate: str
    endDate: str | None

class MedicineListResponseSchema(BaseModel):
    status: str
    medicines: list[MedicineSchema]

class MedicineResponseSchema(BaseModel):
    status: str
    medicine: MedicineSchema | None