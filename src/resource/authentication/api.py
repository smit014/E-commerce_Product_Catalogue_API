from typing import Annotated
from fastapi import APIRouter, Depends
from src.utils.validator import authorization
from src.functionality.authentication.auth import login_user, change_password
from src.resource.authentication.schema import (
    UserLoginRequest,
    ChangePasswordRequest,
)

auth_router = APIRouter()


@auth_router.post("/login", status_code=200)
def login_api(user_data: UserLoginRequest):
    user_info = login_user(user_data.model_dump())
    return user_info


@auth_router.post("/change_password", status_code=201)
def change_password_api(
    user_data: ChangePasswordRequest,
    user_details: Annotated[dict, Depends(authorization)],
):
    user_info = change_password(user_data.model_dump(), user_details.get("id"))
    return user_info
