from pydantic import BaseModel, EmailStr, constr
from datetime import datetime
from typing import Annotated
from pydantic import Field

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: Annotated[str, Field(min_length=6, max_length=72)]

class UserLogin(BaseModel):
    email: EmailStr
    password: str


class ClassCreate(BaseModel):
    name: str
    dateTime: datetime
    instructor: str
    availableSlots: int


class BookingCreate(BaseModel):
    class_id: int
