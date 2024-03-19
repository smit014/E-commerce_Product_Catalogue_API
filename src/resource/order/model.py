from database.database import Base
from sqlalchemy import Column,String,DateTime,ForeignKey,Float,Integer
from datetime import datetime
from src.resource.user.model import User
from src.resource.product.model import Product


class Order(Base):
    __tablename__ = 'orders'
    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey(User.id), nullable=False)
    total_amount = Column(Float, nullable=False)
    status = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())


class OrderItem(Base):
    __tablename__ = 'order_items'
    id = Column(String, primary_key=True)
    order_id = Column(String, ForeignKey(Order.id), nullable=False)
    product_id = Column(String, ForeignKey(Product.id), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
    total_price = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.now())

