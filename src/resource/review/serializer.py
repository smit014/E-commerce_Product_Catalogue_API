def serializer_for_review(review_data):
    if not isinstance(review_data, list):
        review_data = [review_data]
    filter_data=[]
    
    for record in review_data:
        filter_data.append(
            {
                "id":record.id,
                "content" :record.content,
                "rating":record.rating,
                "user_id " :record.user_id,
                "updated_at":str(record.updated_at),
            }
        )
    return filter_data