import uuid
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from database.database import Sessionlocal
from src.resource.order.model import Order, OrderItem
from src.resource.product.model import Product
from datetime import datetime
from src.resource.cart.model import Cart
from src.resource.order.serializer import serializer_for_order

db = Sessionlocal()


def create_order_from_cart(cart_id, user_id):
    cart = db.query(Cart).filter_by(id=cart_id, status="active").first()

    if cart:
        if cart.user_id == user_id:
            id = str(uuid.uuid4())
            order = Order(
                id=id,
                user_id=cart.user_id,
                cart_id=cart.id,
                total_amount=cart.total_amount,
                status="pending",
                created_at=datetime.now(),
                updated_at=datetime.now(),
            )
            db.add(order)
            db.commit()
            cart.status = "ordered"
            db.commit()

            for cart_item in cart.cart_items:
                product = db.query(Product).filter_by(id=cart_item.product_id).first()
                if product:
                    id = str(uuid.uuid4())
                    order_item = OrderItem(
                        id=id,
                        order_id=order.id,
                        product_id=product.id,
                        quantity=cart_item.quantity,
                        unit_price=product.price,
                        total_price=cart_item.quantity * product.price,
                        created_at=datetime.now(),
                        updated_at=datetime.now(),
                    )
                    db.add(order_item)
            db.commit()

            return JSONResponse(
                {"Message": "Order created successfully", "id": str(order.id)}
            )
        else:
            raise HTTPException(status_code=403, detail="you can't accessed this cart")
    else:
        return HTTPException(status_code=404, detail="Cart not found or not active")


def get_order_data_with_item(user_id):
    order_data = (
        db.query(Order)
        .filter(
            Order.user_id == user_id,
        )
        .all()
    )
    order_list = []
    if order_data:
        for order in order_data:
            order_items = db.query(OrderItem).filter_by(order_id=order.id).all()

            filter_data = serializer_for_order(order, order_items)
            order_list.append(filter_data)

        return JSONResponse({"Data": order_list})
    else:
        raise HTTPException(status_code=404, detail="Order not found")


def delete_order(order_id, user_id):

    order_data = db.query(Order).filter_by(id=order_id).first()
    if order_data:
        if order_data.user_id == user_id:
            cart_data = db.query(Cart).filter_by(id=order_data.cart_id).first()
            cart_data.status = "canceled"
            order_item_data = db.query(OrderItem).filter_by(order_id=order_id).all()
            db.delete(order_data)
            for item in order_item_data:
                db.delete(item)
            db.commit()
            return JSONResponse({"Message": "Order deleted"})
        else:
            raise HTTPException(
                status_code=403, detail="you  can't accessed this order"
            )
    else:
        raise HTTPException(status_code=404, detail="Order not found")
