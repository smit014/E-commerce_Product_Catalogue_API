from fastapi import APIRouter, Depends
from typing import Annotated
from src.functionality.product.product import (
    create_product,
    get_product,
    delete_product,
    update_product,
)
from src.resource.product.schema import (
    ProductRequest,
    ProductViewRequest,
    ProductUpdateRequest,
)
from src.utils.validator import authorization

product_router = APIRouter()


@product_router.post("/product", status_code=201)
def create_product_api(
    product_details: ProductRequest, user_data: Annotated[dict, Depends(authorization)]
):
    product_info = create_product(product_details.model_dump(), user_data)
    return product_info


@product_router.get("/product", status_code=200)
def view_product_api(product_details: ProductViewRequest):
    product_info = get_product(product_details.model_dump())
    return product_info


@product_router.patch("/product/{product_id}", status_code=200)
def upadte_product_api(
    product_id: str,
    product_detail: ProductUpdateRequest,
    user_data: Annotated[dict, Depends(authorization)],
):
    product_info = update_product(product_id, product_detail.model_dump(), user_data)
    return product_info


@product_router.delete("/product/{product_id}", status_code=204)
def delete_product_api(
    product_id: str, user_data: Annotated[dict, Depends(authorization)]
):
    product_info = delete_product(product_id, user_data)
    return product_info
