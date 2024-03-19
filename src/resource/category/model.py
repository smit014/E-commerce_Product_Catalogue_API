from database.database import Base
from sqlalchemy import Column,String,VARCHAR,DateTime,ForeignKey
from datetime import datetime
from src.resource.user.model import User

class Category(Base):
    __tablename__ = 'categories'
    id = Column(String, primary_key=True)
    name = Column(VARCHAR(50), nullable=False)
    description = Column(String, nullable=True)
    user_id = Column(String, ForeignKey(User.id), nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
