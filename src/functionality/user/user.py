from database.database import Sessionlocal
from src.resource.user.model import User
from werkzeug.security import generate_password_hash
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from src.resource.authentication.serializer import serializer_for_getuser
from src.config import Config
import uuid
db = Sessionlocal()

def create_admin(admin_details):
    id = str(uuid.uuid4())
    is_admin = admin_details.get('admin_key') == Config.ADMIN_SECRET_KEY
    if not is_admin:
        raise HTTPException(status_code=401, detail="Admin key is required to become a ADMIN")
    if not  admin_details.get("email") or admin_details.get("phone_no"):
        raise HTTPException(status_code=422,detail="add email or phone number")
    if not admin_details.get("password"):
        raise HTTPException(status_code=422 ,detail="Password is required")
    
    user_info = User(
        id = id,
        first_name=admin_details.get('first_name'),
        last_name=admin_details.get('last_name'),
        name=admin_details.get('name'),
        email=admin_details.get('email'),
        phone_no=admin_details.get('phone_no'),
        password=generate_password_hash(admin_details.get('password')),
        is_admin=is_admin,
    )
    db.add(user_info)
    db.commit()
    db.close()
    return {"Message": "Admin user created successfully"}


def create_user(user_details):
    id = str(uuid.uuid4())
    if not  user_details.get("email") or user_details.get("phone_no"):
        raise HTTPException(status_code=422,detail="add email or phone number")
    if not user_details.get("password"):
        raise HTTPException(status_code=422 ,detail="Password is required")
    
    user_info = User(
        id = id,
        first_name=user_details.get('first_name'),
        last_name=user_details.get('last_name'),
        name=user_details.get('name'),
        email=user_details.get('email'),
        phone_no=user_details.get('phone_no'),
        password=generate_password_hash(user_details.get('password')),
    )
    db.add(user_info)
    db.commit()
    db.close()
    return {"Message": "User created successfully"}


def get_user(user_id):
    user_data = (
        db.query(User).filter_by(id=user_id, is_active=True, is_deleted=False).first()
    )
    if user_data:
        filter_data = serializer_for_getuser(user_data)
        
        return JSONResponse({"Data": filter_data})

    else:
        raise HTTPException(status_code=404, detail="User not found")
    

def delete_user(user_id,user_details):
    if user_id == user_details.get("id"):
        user_data = (
            db.query(User).filter_by(id=user_id, is_active=True, is_deleted=False).first()
        )
        if user_data:
            user_data.is_active = False
            user_data.is_deleted =True
            db.commit()
            db.close()
            return JSONResponse({"Message": "User deleted successfully"})
    else:
        raise HTTPException(status_code=409,detail="Invalid user id")

