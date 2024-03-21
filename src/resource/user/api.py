from fastapi import APIRouter, Depends
from typing import Annotated
from src.resource.user.schema import UserRequest,AdminRequest
from src.utils.validator import authorization
from src.functionality.user.user import create_user, get_user,delete_user

user_router = APIRouter()


@user_router.post("/signup", status_code=201)
def create_user_api(user_data: UserRequest):
    user_info = create_user(user_data.model_dump())
    return user_info

@user_router.post("/admin", status_code=201)
def create_user_api(admin_data: AdminRequest):
    admin_info = create_user(admin_data.model_dump())
    return admin_info

@user_router.get("/get_user", status_code=200)
def get_user_api(user_data: Annotated[dict, Depends(authorization)]):
    user_info = get_user(user_data.get("id"))
    return user_info

@user_router.delete("/user_details/{user_id}", status_code=204)
def delete_user_api(user_id :str,user_data: Annotated[dict, Depends(authorization)]):
    user_info = delete_user(user_id,user_data)
    return user_info
