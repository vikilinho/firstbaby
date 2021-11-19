from pydantic import BaseModel
from typing import Optional


class User (BaseModel):
    fullName: str
    age: int
    email: str
    sex: Optional[str]
