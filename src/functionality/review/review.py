import uuid
from database.database import Sessionlocal
from src.resource.review.model import Review
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from datetime import datetime
from src.resource.review.serializer import serializer_for_review


db = Sessionlocal()

def create_review(review_details,user_details):
    id = uuid.uuid4()
    review_data = db.query(Review).filter_by(product_id = review_details.get('product_id'),user_id = user_details.get('id')).first()
    if not review_data:
        review_info = Review(
            id = id,
            content = review_details.get('content'),
            rating = review_details.get('rating'),
            product_id = review_details.get('product_id'),
            user_id = user_details.get('id'),
        )
        db.add(review_info)
        db.commit()
        return JSONResponse({"Message":"Review created successfully","Review_id ":str(id)})
    else:
        raise HTTPException(status_code=403,detail="you already have a review so you can't create a new review")

def show_reviews(product_id):
    review_data = db.query(Review).filter_by(product_id = product_id).all()

    if review_data:
        filter_data = serializer_for_review(review_data)
        return JSONResponse({"Data": filter_data})
    else :
        raise HTTPException(status_code = 404,detail="No review yet available")
    
def get_review(review_id):
    review_data = db.query(Review).filter_by(id = review_id).first()
    if review_data:
        filter_data = serializer_for_review(review_data)
        return JSONResponse({"Data": filter_data})
    else :
        raise HTTPException(status_code = 404,detail="Review not found")
    

def update_review(review_details,review_id,user_id):
    review_data = db.query(Review).filter_by(id = review_id).first()
    if review_data:
        if review_data.user_id == user_id :
            review_data.content = review_details.get("content") if review_details.get("content") is not None else review_data.content
            review_data.rating = review_details.get("rating") if review_details.get("rating") is not None else review_data.rating
            review_data.updated_at = datetime.now()
            db.commit()
            db.close()
            return JSONResponse({"Message":" Review updated Succesfully "})
        else:
            raise HTTPException(status_code=403,detail="You have not rights to update this Review")
    else:
        raise HTTPException(status_code=404,detail="Review not found")


def delete_review(review_id,user_id):
    review_data = db.query(Review).filter_by(id=review_id).first()
    if review_data:
        if review_data.user_id == user_id:
            db.delete(review_data)
            db.commit()
            return JSONResponse({"Message":" Review deleted"})
        else:
            raise HTTPException(status_code=403,detail="you cannot delete this review")
    else:
        raise HTTPException(status_code=404,detail="Review not found")
