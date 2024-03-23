from pydantic import BaseModel
from typing import Optional


class UserLoginRequest(BaseModel):
    phone_no: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str]


class ChangePasswordRequest(BaseModel):
    password: str
    new_password: str
