from fastapi import APIRouter, Depends
from typing import Annotated
from src.resource.category.schema import CategoryRequest
from src.utils.validator import authorization
from src.functionality.category.category import create_category,view_category

category_router =APIRouter()

@category_router.post("/category",status_code=201)
def create_category_api(category_data :CategoryRequest,user_data: Annotated[dict, Depends(authorization)],):
    category_info = create_category(category_data.model_dump(),user_data)
    return category_info


@category_router.get("/category",status_code=201)
def view_category_api():
    category_info = view_category()
    return category_info


@category_router.patch("/category",status_code=201)
def update_category_api():
    pass


@category_router.delete("/category",status_code=204)
def delete_category_api():
    pass