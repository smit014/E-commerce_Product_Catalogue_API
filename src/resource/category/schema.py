from pydantic import BaseModel
from typing import Optional


class CategoryRequest(BaseModel):
    
    name : Optional[str]=None  
    description : Optional[str]= None