def serializer_for_category(category_data):
    if not isinstance(category_data, list):
        category_data = [category_data]
    filter_data = []

    for record in category_data:
        filter_data.append(
            {
                "id": record.id,
                "name": record.name,
                "description": record.description,
                "user_id ": record.user_id,
                "updated_at": str(record.updated_at),
            }
        )
    return filter_data
