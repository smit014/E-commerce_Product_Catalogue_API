from database.database import Base
from sqlalchemy import Column, String, VARCHAR, Boolean, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True)
    first_name = Column(VARCHAR(30))
    last_name = Column(VARCHAR(30))
    name = Column(VARCHAR(30))
    phone_no = Column(VARCHAR(255))
    email = Column(String(256), nullable=False)
    password = Column(VARCHAR(8012), nullable=False)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)

    cart = relationship("Cart", back_populates="user")
    orders = relationship("Order", back_populates="user")
