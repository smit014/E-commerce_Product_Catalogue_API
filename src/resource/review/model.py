from database.database import Base
from sqlalchemy import Column,String,DateTime,ForeignKey,Integer
from datetime import datetime
from src.resource.product.model import Product
from src.resource.user.model import User

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(String, primary_key=True)
    content = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)
    product_id = Column(String, ForeignKey(Product.id), nullable=False)
    user_id = Column(String, ForeignKey(User.id), nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
