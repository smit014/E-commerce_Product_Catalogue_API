from database.database import Sessionlocal
from src.resource.product.model import Product
from src.resource.cart.model import Cart,CartItem
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from datetime import datetime
import uuid
from src.resource.cart.serializer import serializer_for_cart


db = Sessionlocal()

def add_item_to_cart(item_data):
    try:
        product_id = item_data.get("product_id")
        product_data = db.query(Product).filter_by(id=product_id).first()
        if not product_data:
            raise HTTPException(status_code=404, detail="Product not found")
        cart = db.query(Cart).filter_by(user_id=item_data.get("user_id"), status="active").first()
        product = db.query(CartItem).filter_by(product_id=product_id,cart_id= cart.id).first()
        if product:
            raise HTTPException(status_code=403,detail="Product  is already exists in cart")

        if not cart:
            id = str(uuid.uuid4())
            cart = Cart(id=id,user_id=item_data.get("user_id"), total_amount=0.0, status="active")
            db.add(cart)
            db.commit()

        if cart:
            id = str(uuid.uuid4())
            cart_item = CartItem(
                id=id,
                cart_id=cart.id,
                product_id=item_data.get("product_id"),
                quantity=item_data.get("quantity"),
                unit_price=product_data.price,
                total_price=item_data.get("quantity") * product_data.price,
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
            db.add(cart_item)
            db.commit()

        cart.total_amount += cart_item.total_price
        db.commit()
        return {"message": "Item added to cart successfully"}
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    
def update_cart_item( item_data):
    item_id = item_data.get("item_id")
    cart_id = item_data.get("cart_id")
    cart_item = db.query(CartItem).filter_by(id=item_id, cart_id=cart_id).first()
    if not cart_item:
        raise HTTPException(status_code=404, detail="Cart item not found")

    cart = db.query(Cart).filter_by(id=cart_id).first()
    cart.total_amount -= cart_item.total_price
    cart_item.quantity = item_data.get("quantity")if item_data.get("quantity") is not None else cart_item.quantity 
    cart_item.total_price = cart_item.quantity * cart_item.unit_price
    cart_item.updated_at = datetime.now()

    cart.total_amount += cart_item.total_price
    db.commit()

    return JSONResponse({"Message":"Cart item updated"})

def delete_cart_item(item_data):
    item_id = item_data.get("item_id")
    cart_id = item_data.get("cart_id")
    cart_item = db.query(CartItem).filter_by(id=item_id, cart_id=cart_id).first()
    if not cart_item:
        raise HTTPException(status_code=404, detail="Cart item not found")

    cart = db.query(Cart).filter_by(id=cart_id).first()
    cart.total_amount -= cart_item.total_price
    db.commit()
    db.delete(cart_item)
    db.commit()

    return JSONResponse({"Message":"Cart item deleted"})

def get_cart_with_items( cart_id: str):
    cart = db.query(Cart).filter_by(id=cart_id).first()
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")

    
    cart_items = db.query(CartItem).filter_by(cart_id=cart_id).all()

    filter_data =serializer_for_cart(cart,cart_items)

    return JSONResponse({"Data":filter_data})
