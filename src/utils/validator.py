from fastapi import HTTPException, Header
import jwt
from src.config import Config
from database.database import Sessionlocal
from src.resource.user.model import User

db = Sessionlocal()


def authorization(Authorization=(Header(..., description="Authorization"))):
    
    token = Authorization.split(" ")[1]
    decode_token = jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=["HS256"])

    user_data = (
        db.query(User)
        .filter(
            User.id == decode_token["id"],
            User.is_active == True,
            User.is_deleted == False,
        )
        .first()
    )
    if not user_data:
        raise HTTPException(status_code=403,detail="Authentication failed")

    user_dict = user_data.__dict__

    user_dict.pop('_sa_instance_state', None)

    return user_dict
