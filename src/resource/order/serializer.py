def serializer_for_order(order_data, order_item_data):
    order_data = order_data if isinstance(order_data, list) else [order_data]
    order_item_data = order_item_data if isinstance(order_item_data, list) else [order_item_data]

    filter_data = [{
        "id": order.id,
        "user_id": order.user_id,
        "total_amount": order.total_amount,
        "status": order.status,
        "updated_at": str(order.updated_at),
        "items": [{
            "id": item.id,
            "product_id": item.product_id,
            "order_id": item.order_id,
            "quantity": item.quantity,
            "unit_price": item.unit_price,
            "total_price": item.total_price,
            "updated_at": str(item.updated_at),
        } for item in order_item_data if item.order_id == order.id]
    } for order in order_data]

    return filter_data


    # for order in orders:
    # order_items = []
    # for item in order.order_items:
    #     product = db.query(Product).filter(Product.id == item.product_id).first()
    #     order_items.append({
    #         "product_id": item.product_id,
    #         "product_name": product.name if product else "Product not found",
    #         "quantity": item.quantity,
    #         "unit_price": item.unit_price,
    #         "total_price": item.total_price
    #     })

    # order_data.append({
    #     "order_id": order.id,
    #     "total_amount": order.total_amount,
    #     "status": order.status,
    #     "order_items": order_items
    # })