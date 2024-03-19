from fastapi import APIRouter

product_router = APIRouter

@product_router.post("/product",status_code=201)
def create_product():
    pass


@product_router.get("/product",status_code=200)
def view_product():
    pass


@product_router.patch("/product",status_code=201)
def upadte_product():
    pass


@product_router.delete("/product",status_code=204)
def delete_product():
    pass