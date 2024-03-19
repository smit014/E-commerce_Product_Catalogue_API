import uuid
from src.resource.category.model import Category
from src.resource.category.serializer import serializer_for_category
from database.database  import Sessionlocal
from fastapi import HTTPException
from fastapi.responses import JSONResponse

db = Sessionlocal()

def create_category(category_details,user_details):
    id = str(uuid.uuid4())

    if user_details.get("is_admin"):
        
        catgory_info = Category(
            id = id,
            name = category_details.get('name'),
            description = category_details.get('description'),
            user_id = user_details.get('id'),
        )
        db.add(catgory_info)
        db.commit()
        db.close()

        return {"Message": "category created successfully"}
    else:
        raise HTTPException(status_code=403,detail="you are not allowed to create")

def view_category():
    category_data = db.query(Category).all()
    if category_data:
        filter_data = serializer_for_category(category_data)
        return JSONResponse({"Data": filter_data})
    else:
        raise HTTPException(status_code=404,detail="categorys not found")


def update_category():
    pass


def delete_category(category_id,user_details):
    if user_details.get("is_admin"):
        category_data = db.query(Category).filter_by(id = category_id).first()
        if category_data:
            del category_data
            db.commit()
            return JSONResponse({"Message": "category deleted successfully"})
        else:
            raise HTTPException (status_code=404,detail="Category not found")
    else:
        raise HTTPException(status_code=403,detail="you have no rights to delete it")

