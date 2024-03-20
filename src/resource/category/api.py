from fastapi import APIRouter, Depends
from typing import Annotated
from src.resource.category.schema import CategoryRequest
from src.utils.validator import authorization
from src.functionality.category.category import (
    create_category,
    get_category,
    delete_category,
    update_category,
    get_all_category,
)

category_router = APIRouter()


@category_router.post("/category", status_code=201)
def create_category_api(
    category_data: CategoryRequest, user_data: Annotated[dict, Depends(authorization)]
):
    category_info = create_category(category_data.model_dump(), user_data)
    return category_info


@category_router.get("/category", status_code=200)
def get_all_category_api():
    category_info = get_all_category()
    return category_info

@category_router.get("/category/{category_id}", status_code=200)
def get_category_api(category_id:str):
    category_info = get_category(category_id)
    return category_info


@category_router.patch("/category/{category_id}", status_code=201)
def update_category_api(
    category_data: CategoryRequest,
    category_id: str,
    user_data: Annotated[dict, Depends(authorization)],
):
    category_info = update_category(category_data.model_dump(), category_id, user_data)
    return category_info


@category_router.delete("/category/{category_id}", status_code=204)
def delete_category_api(
    category_id: str,
    user_data: Annotated[dict, Depends(authorization)]
):
    category_info = delete_category(category_id, user_data)
    return category_info
