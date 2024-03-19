from pydantic import BaseModel
from typing import Optional     


class UserRequest(BaseModel):
    
    name : Optional[str]
    first_name : Optional[str]
    last_name : Optional[str]
    phone_no : int
    email : Optional[str]
    password : str
    is_admin : Optional[bool] = False
    admin_key : Optional[str]