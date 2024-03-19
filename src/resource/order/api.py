from fastapi import APIRouter

order_router = APIRouter()


@order_router.post("/order",status_code=201)
def create_order():
    pass


@order_router.get("/order",status_code=201)
def create_order():
    pass

@order_router.patch("/order",status_code=201)
def create_order():
    pass


@order_router.delete("/order",status_code=201)
def create_order():
    pass
