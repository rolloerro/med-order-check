from pydantic import BaseModel
from typing import List, Optional

class Medication(BaseModel):
    name: str
    dose_mg: float
    frequency_per_day: int

class Patient(BaseModel):
    age: int
    sex: str  # male / female

class OrderCheckRequest(BaseModel):
    patient: Patient
    diagnoses: List[str]
    medications: List[Medication]

class Issue(BaseModel):
    level: str  # warning / error
    message: str

class OrderCheckResponse(BaseModel):
    issues: List[Issue]
    severity: str  # low / medium / high
