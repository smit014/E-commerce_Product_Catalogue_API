from database.database import Sessionlocal
from src.resource.user.model import User
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import or_
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from src.resource.authentication.serializer import serializer_for_login
from src.resource.authentication.jwt_token import generate_token

db = Sessionlocal()


def login_user(user_details):
    email = user_details.get("email")
    phone_no = user_details.get("phone_no")
    password = user_details.get("password")

    if email or phone_no:
        user_data = (
            db.query(User)
            .filter(
                or_((User.email == email), (User.phone_no == phone_no)),
                User.is_active == True,
                User.is_deleted == False,
            )
            .first()
        )

        if user_data:
            if check_password_hash(user_data.password, password):
                filtered_data = serializer_for_login(user_data)
                access_token = generate_token(filtered_data, 7)
                refresh_token = generate_token(filtered_data, 30)
                db.commit()
                db.close()
                return JSONResponse(
                    {"Access_Token": access_token, "Refresh_token": refresh_token},
                    status_code=200,
                )
            else:
                raise HTTPException(status_code=401, detail="Incorrect password")
        else:
            raise HTTPException(status_code=404, detail="User not found")
    else:
        raise HTTPException(status_code=400, detail="Email or phone number is required")


def change_password(user_details, user_id):
    password = user_details.get("password")
    new_password = generate_password_hash(user_details.get("new_password"))

    user_data = None
    if user_id:
        user_data = (
            db.query(User)
            .filter_by(id=user_id, is_active=True, is_deleted=False)
            .first()
        )
        if user_data:
            if password == user_details.get("new_password"):
                raise HTTPException(
                            status_code=401,
                            detail="Old Password and New Password has to be Different",
                        )
            else:
                if check_password_hash(user_data.password, password):
                    user_data.password = new_password
                    db.commit()
                    db.close()
                    return JSONResponse({"Message": "password successfully changed"}, status_code=200)
                else:
                    raise HTTPException(status_code=401, detail="Incorrect password")
        else:
            raise HTTPException(status_code=404, detail="User not found")
    else:
        raise HTTPException(status_code=407,detail="Login with correct user data")

        # if user_data:
        #     if check_password_hash(user_data.password, password):
        #         if password == user_details.get("new_password"):
        #             raise HTTPException(
        #                 status_code=401,
        #                 detail="Old Password and New Password has to be Different",
        #             )

        #         user_data.password = new_password
        #         db.commit()
        #         db.close()
        #         return JSONResponse(
        #             {"Message": "password successfully changed"}, status_code=200
        #         )

        #     else:
        #         raise HTTPException(status_code=401, detail="Incorrect password")