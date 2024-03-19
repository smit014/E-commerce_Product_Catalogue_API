import jwt 
from datetime import datetime, timedelta
from src.config import Config

def generate_token(user_data,exp):
    expires_delta = timedelta(days=exp)
    user_data['exp'] = datetime.now() + expires_delta   
    
    data = user_data
    encode_data = jwt.encode(data, Config.JWT_SECRET_KEY, algorithm="HS256")
    
    return encode_data