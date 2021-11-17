from pydantic import BaseModel
from typing import Optional


class Registration (BaseModel):
    fullName: str
    age: int
    email: str
    sex: Optional[str]
    password: str
    confirmPassword: str
