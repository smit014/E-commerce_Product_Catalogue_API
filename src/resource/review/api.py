from fastapi import APIRouter, Depends
from typing import Annotated
from src.resource.review.schema import ReviewRequest, ReviewUpdate
from src.utils.validator import authorization
from src.functionality.review.review import (
    create_review,
    get_review,
    show_reviews,
    update_review,
    delete_review,
)

review_router = APIRouter()


@review_router.post("/review", status_code=201)
def create_review_api(
    review_details: ReviewRequest, user_data: Annotated[dict, Depends(authorization)]
):
    review_info = create_review(review_details.model_dump(), user_data)
    return review_info


@review_router.get("/allreview/{product_id}", status_code=200)
def show_review_api(product_id: str):
    review_info = show_reviews(product_id)
    return review_info


@review_router.get("/review/{review_id}", status_code=200)
def get_review_api(review_id: str):
    review_info = get_review(review_id)
    return review_info


@review_router.patch("/review/{review_id}", status_code=200)
def update_review_api(
    review_details: ReviewUpdate,
    review_id: str,
    user_data: Annotated[dict, Depends(authorization)],
):
    review_info = update_review(
        review_details.model_dump(), review_id, user_data.get("id")
    )
    return review_info


@review_router.delete("/review/{review_id}", status_code=204)
def delete_review_api(
    review_id: str, user_data: Annotated[dict, Depends(authorization)]
):
    review_info = delete_review(review_id, user_data.get("id"))
    return review_info
