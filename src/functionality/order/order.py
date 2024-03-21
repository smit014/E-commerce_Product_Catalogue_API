import uuid
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from database.database import Sessionlocal
from src.resource.order.model import Order, OrderItem
from src.resource.product.model import Product
from datetime import datetime

db = Sessionlocal()
def create_order(order_data):
    try:
        order_id = str(uuid.uuid4())  
        order = Order(
            id=order_id,
            user_id=order_data.user_id,
            total_amount=0.0,  
            status="pending",
        )
        db.add(order)
        db.commit()
        db.refresh(order)

        # Add order items to the order
        for product_id, item_data in order_data.order_items.items():
            product = db.query(Product).filter_by(id=item_data.product_id).first()
            if product:
                order_item_id = str(uuid.uuid4())  # Generate unique order item ID
                order_item = OrderItem(
                    id=order_item_id,
                    order_id=order.id,
                    product_id=item_data.product_id,
                    quantity=item_data.quantity,
                    unit_price=product.price,
                    total_price=item_data.quantity * product.price,
                    created_at=datetime.now(),
                )
                db.add(order_item)
                db.commit()
                # Update the total amount of the order
                order.total_amount += order_item.total_price

        # Update the order with the calculated total amount
        db.commit()
        db.refresh(order)

        # Return success message with order details
        return JSONResponse(
            status_code=200,
            content={"message": "Order created successfully"},
        )

    except Exception as e:
        # Rollback changes if an error occurs
        db.rollback()
        # Raise HTTPException with error message
        raise HTTPException(
            status_code=400,
            detail=f"Failed to create order: {str(e)}",
        )
