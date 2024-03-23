from database.database import Base
from sqlalchemy import Column, String, DateTime, ForeignKey, Float, Integer
from datetime import datetime
from src.resource.user.model import User
from src.resource.product.model import Product
from src.resource.cart.model import Cart
from sqlalchemy.orm import relationship


class Order(Base):
    __tablename__ = "orders"
    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey(User.id, ondelete="CASCADE"), nullable=False)
    cart_id = Column(
        String,
        ForeignKey(
            Cart.id,
        ),
    )
    total_amount = Column(Float, nullable=False)
    status = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())

    # Define one-to-many relationship with OrderItem
    user = relationship("User", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="order")


class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(String, primary_key=True)
    order_id = Column(String, ForeignKey(Order.id, ondelete="CASCADE"), nullable=False)
    product_id = Column(
        String, ForeignKey(Product.id, ondelete="CASCADE"), nullable=False
    )
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
    total_price = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    # Define many-to-one relationship with Order
    order = relationship("Order", back_populates="order_items")
