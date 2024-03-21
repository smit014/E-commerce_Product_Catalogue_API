from fastapi import APIRouter, Depends
from typing import Annotated
from src.utils.validator import authorization
from src.resource.cart.schema import CartItemCreate,CartItemUpdate,CartItemDelete
from src.functionality.cart.cart import add_item_to_cart,update_cart_item,delete_cart_item,get_cart_with_items


cart_router = APIRouter()

@cart_router.post("/cart/add_item",status_code=201)
def add_item_to_cart_api(item_details:CartItemCreate):
    cart_info = add_item_to_cart(item_details.model_dump())
    return cart_info

@cart_router.patch("/cart/upadate_item",status_code=200)
def update_item_to_cart_api(item_details:CartItemUpdate):
    cart_info = update_cart_item(item_details.model_dump())
    return cart_info

@cart_router.delete("/cart/delete_item",status_code=403)
def delete_item_to_cart_api(item_details:CartItemDelete):
    cart_info = delete_cart_item(item_details.model_dump())
    return cart_info

@cart_router.get("/cart/{cart_id}",status_code=200)
def get_cart(cart_id:str):
    cart_info = get_cart_with_items(cart_id)
    return cart_info
