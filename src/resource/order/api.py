from fastapi import APIRouter,HTTPException
from src.functionality.order.order import create_order
from src.resource.order.schema import OrderCreate,OrderItemCreate
order_router = APIRouter()


@order_router.post("/order",status_code=201)
def create_order_api(order_data: OrderCreate):
    
    # Call the create_order function from your order functionality module
    order_info = create_order(order_data)
    return order_info



# @order_router.get("/order",status_code=201)
# def create_order():
#     pass

# @order_router.patch("/order",status_code=201)
# def create_order():
#     pass


# @order_router.delete("/order",status_code=201)
# def create_order():
#     pass
