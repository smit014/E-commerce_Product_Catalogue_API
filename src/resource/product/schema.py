from pydantic import BaseModel
from typing import Optional

class ProductRequest(BaseModel):
    name : str
    description : Optional[str]
    price :float
    stock_quantity : int
    image : str
    category_id : str


class ProductViewRequest(BaseModel):
    category_id : str
    min_price : Optional[float]=None
    max_price : Optional[float]=None


class ProductUpdateRequest(BaseModel):
    name : str
    description : Optional[str]=None
    price :Optional[float]=None
    stock_quantity : Optional[int]=None
    categoery_id : Optional[str]=None
    image : Optional[str]=None