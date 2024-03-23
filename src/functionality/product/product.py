import uuid
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from database.database import Sessionlocal
from src.resource.product.serializer import serializer_for_product
from src.resource.product.model import Product
from datetime import datetime


db = Sessionlocal()


def create_product(product_details, user_details):
    id = str(uuid.uuid4())
    if user_details.get("is_admin"):
        try:
            product_info = Product(
                id=id,
                name=product_details.get("name"),
                description=product_details.get("description"),
                price=product_details.get("price"),
                stock_quantity=product_details.get("stock_quantity"),
                category_id=product_details.get("category_id"),
                user_id=user_details.get("id"),
                image=product_details.get("image"),
            )
            db.add(product_info)
            db.commit()
            return JSONResponse(
                {"Message": "Product created successfully", "id": str(id)}
            )
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=400, detail="Enter the mandatory fields")
        finally:
            db.close()
    else:
        raise HTTPException(status_code=403, detail="you are not allowed to create")


def get_product(product_details):
    if product_details.get("category_id"):
        query = db.query(Product).filter_by(
            category_id=product_details.get("category_id")
        )
        if product_details.get("min_price") is not None:
            query = query.filter(Product.price >= product_details.get("min_price"))
        if product_details.get("max_price") is not None:
            query = query.filter(Product.price <= product_details.get("max_price"))
        product_data = query.all()
        if product_data:
            filter_data = serializer_for_product(product_data)
            return JSONResponse({"Data": filter_data})
        else:
            raise HTTPException(status_code=404, detail="product not found")
    else:
        raise HTTPException(status_code=404, detail="category not found")


def update_product(product_id, product_detail, user_details):
    if user_details.get("is_admin"):
        product_data = db.query(Product).filter_by(id=product_id).first()
        if product_data:
            product_data.name = product_detail.get("name")
            product_data.description = (
                product_detail.get("description")
                if product_detail.get("description") is not None
                else product_data.description
            )
            product_data.price = (
                product_detail.get("price")
                if product_detail.get("price") is not None
                else product_data.price
            )
            product_data.stock_quantity = (
                product_detail.get("stock_quantity")
                if product_detail.get("stock_quantity") is not None
                else product_data.stock_quantity
            )
            product_data.category_id = (
                product_detail.get("category_id")
                if product_detail.get("category_id") is not None
                else product_data.category_id
            )
            product_data.image = (
                product_detail.get("image")
                if product_detail.get("image") is not None
                else product_data.image
            )
            product_data.updated_at = datetime.now()
            db.commit()
            db.close()
            return JSONResponse({"Message": "product upadate successfully"})
        else:
            raise HTTPException(status_code=404, detail="product not found")
    else:
        raise HTTPException(status_code=401, detail="you have no rights to upadate it")


def delete_product(product_id, user_details):
    if user_details.get("is_admin"):
        category_data = db.query(Product).filter_by(id=product_id).first()
        if category_data:
            db.delete(category_data)
            db.commit()
            return JSONResponse({"Message": "product deleted successfully"})
        else:
            raise HTTPException(status_code=404, detail="product not found")
    else:
        raise HTTPException(status_code=403, detail="you have no rights to delete it")
