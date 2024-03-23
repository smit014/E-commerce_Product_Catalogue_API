from database.database import Base
from sqlalchemy import Column, String, VARCHAR, DateTime, ForeignKey, Float, Integer
from datetime import datetime
from src.resource.category.model import Category
from src.resource.user.model import User


class Product(Base):
    __tablename__ = "products"
    id = Column(String, primary_key=True)
    name = Column(VARCHAR(100), nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, default=0)
    category_id = Column(String, ForeignKey(Category.id), nullable=False)
    user_id = Column(String, ForeignKey(User.id), nullable=False)
    image = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
