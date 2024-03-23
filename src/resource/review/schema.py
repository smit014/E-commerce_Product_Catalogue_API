from pydantic import BaseModel
from typing import Optional


class ReviewRequest(BaseModel):
    product_id: str
    content: str
    rating: float


class ReviewUpdate(BaseModel):
    content: Optional[str] = None
    rating: Optional[float] = None
