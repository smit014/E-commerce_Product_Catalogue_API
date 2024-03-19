from fastapi import APIRouter

review_router = APIRouter

@review_router.post("/review",status_code=201)
def create_review():
    pass

@review_router.get("/review",status_code=200)
def view_review():
    pass

@review_router.patch("/review",status_code=201)
def update_review():
    pass

@review_router.delete("/review",status_code=204)
def delete_review():
    pass