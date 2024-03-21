def serializer_for_cart(cart_data, cart_item_data):
    cart_data = cart_data if isinstance(cart_data, list) else [cart_data]
    cart_item_data = cart_item_data if isinstance(cart_item_data, list) else [cart_item_data]

    filter_data = [{
        "id": cart.id,
        "user_id": cart.user_id,
        "total_amount": cart.total_amount,
        "status": cart.status,
        "updated_at": str(cart.updated_at),
        "items": [{
            "id": item.id,
            "product_id": item.product_id,
            "quantity": item.quantity,
            "unit_price": item.unit_price,
            "total_price": item.total_price,
            "updated_at": str(item.updated_at),
        } for item in cart_item_data if item.cart_id == cart.id]
    } for cart in cart_data]

    return filter_data