def serializer_for_product(product_data):
    if not isinstance(product_data, list):
        product_data = [product_data]
    filter_data = []

    for record in product_data:
        filter_data.append(
            {
                "id": record.id,
                "name": record.name,
                "description": record.description,
                "user_id ": record.user_id,
                "price": record.price,
                "stock_quantity": record.stock_quantity,
                "image": record.image,
                "updated_at": str(record.updated_at),
            }
        )
    return filter_data
