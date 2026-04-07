from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    date_of_birth: Optional[date]
    gender: Optional[str]
    company_name: Optional[str]