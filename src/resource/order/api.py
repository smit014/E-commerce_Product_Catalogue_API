from fastapi import APIRouter, Depends
from src.utils.validator import authorization
from typing import Annotated
from src.functionality.order.order import create_order_from_cart,get_order_data_with_item,delete_order
order_router = APIRouter()


@order_router.post("/order",status_code=201)
def create_order_api(cart_id, user_data: Annotated[dict, Depends(authorization)]):
    order_info = create_order_from_cart(cart_id,user_data.get("id"))
    return order_info

@order_router.get("/order/{user_id}",status_code=200)
def get_order_api( user_data: Annotated[dict, Depends(authorization)]):
    order_info = get_order_data_with_item(user_data.get("id"))
    return order_info

@order_router.delete("/order/{order_id}",status_code=204)
def delete_order_api(order_id:str, user_data: Annotated[dict, Depends(authorization)]):
    order_info =delete_order(order_id,user_data.get("id"))
    return order_info