from fastapi import FastAPI
from src.resource.user.api import user_router
from src.resource.authentication.api import auth_router
from src.resource.category.api import category_router
from src.resource.product.api import product_router
from src.resource.review.api import review_router
from src.resource.order.api import order_router
from src.resource.cart.api import cart_router

app = FastAPI()
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(category_router)
app.include_router(product_router)
app.include_router(review_router)
app.include_router(order_router)
app.include_router(cart_router)
