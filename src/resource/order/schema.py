from pydantic import BaseModel
from typing import Dict

class OrderItemCreate(BaseModel):
    product_id: str
    quantity: int

class OrderCreate(BaseModel):
    user_id: str
    order_items: Dict[str, OrderItemCreate]