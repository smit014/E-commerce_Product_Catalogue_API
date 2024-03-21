from pydantic import BaseModel

class CartItemCreate(BaseModel):
    user_id: str
    product_id: str
    quantity: int

class CartItemUpdate(BaseModel):
    cart_id: str
    item_id: str
    quantity: int

class CartItemDelete(BaseModel):
    cart_id: str
    item_id: str