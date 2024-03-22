from pydantic import BaseModel
from typing import Optional     


class UserRequest(BaseModel):
    
    name : Optional[str]
    first_name : Optional[str]
    last_name : Optional[str]
    phone_no : Optional[int]
    email : Optional[str]
    password : Optional[str]
    

class AdminRequest(BaseModel):
    
    name : Optional[str]
    first_name : Optional[str]
    last_name : Optional[str]
    phone_no : Optional[int]
    email : Optional[str]
    password :Optional[str]
    admin_key : Optional[str]