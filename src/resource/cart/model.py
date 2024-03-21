from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Integer, Float,DateTime
from database.database import Base
from src.resource.user.model import User
from src.resource.product.model import Product
from datetime import datetime

class Cart(Base):
    __tablename__ = 'carts'
    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey(User.id, ondelete="CASCADE"), nullable=False)
    total_amount = Column(Float, nullable=False)
    status = Column(String, nullable=False)
    user = relationship("User", back_populates="cart") #one-to-many relationship
    cart_items = relationship("CartItem", back_populates="cart")
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    

class CartItem(Base):
    __tablename__ = 'cart_items'
    id = Column(String, primary_key=True)
    cart_id = Column(String, ForeignKey(Cart.id, ondelete="CASCADE"), nullable=False)
    product_id = Column(String, ForeignKey(Product.id, ondelete="CASCADE"), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
    total_price = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())

    cart = relationship("Cart", back_populates="cart_items")

