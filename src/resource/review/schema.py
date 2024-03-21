from pydantic import BaseModel
from typing import Optional

class ReviewRequest(BaseModel):
    product_id : str
    content : str
    rating : int

class ReviewUpdate(BaseModel):
    content : Optional[str]= None
    rating :Optional[int]= None