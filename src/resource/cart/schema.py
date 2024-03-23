from pydantic import BaseModel


class CartItemCreate(BaseModel):
    product_id: str
    quantity: int


class CartItemUpdate(BaseModel):
    cart_id: str
    item_id: str
    quantity: int


class CartItemDelete(BaseModel):
    cart_id: str
    id: str
