import uuid
from src.resource.category.model import Category
from src.resource.category.serializer import serializer_for_category
from database.database import Sessionlocal
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from datetime import datetime

db = Sessionlocal()

def create_category(category_details, user_details):
    id = str(uuid.uuid4())

    if user_details.get("is_admin"):

        catgory_info = Category(
            id=id,
            name=category_details.get("name"),
            description=category_details.get("description"),
            user_id=user_details.get("id"),
        )
        db.add(catgory_info)
        db.commit()
        db.close()

        return JSONResponse({"Message": "category created successfully","id ":str(id)})
    else:
        raise HTTPException(status_code=403, detail="you are not allowed to create")


def get_all_category():
    category_data = db.query(Category).all()
    if category_data:
        filter_data = serializer_for_category(category_data)
        return JSONResponse({"Data": filter_data})
    else:
        raise HTTPException(status_code=404, detail="categorys not found")
    
def get_category(category_id):
    category_data = db.query(Category).filter_by(id = category_id).first()
    if category_data:
        filter_data = serializer_for_category(category_data)
        return JSONResponse({"Data": filter_data})
    else:
        raise HTTPException(status_code=404, detail="categorys not found")
    



def update_category(category_details, category_id, user_details):
    if user_details.get("is_admin"):
        category_data = db.query(Category).filter_by(id=category_id).first()
        if category_data:
            category_data.name = category_details.get("name") if category_details.get("name") is not None else category_data.name
            category_data.description = category_details.get("description") if category_details.get("description") is not None else category_data.description
            category_data.updated_at = datetime.now()
            db.commit()
            db.close()
            return JSONResponse({"Message": "category upadate successfully"})
        else:
            raise HTTPException(status_code=404, detail="Category not found")
    else:
        raise HTTPException(
            status_code=401, detail="you have no rights to upadate it"
        )


def delete_category(category_id, user_details):
    if user_details.get("is_admin"):
        category_data = db.query(Category).filter_by(id=category_id).first()
        if category_data:
            db.delete(category_data)
            db.commit()
            return JSONResponse({"Message": "category deleted successfully"})
        else:
            raise HTTPException(status_code=404, detail="Category not found")
    else:
        raise HTTPException(status_code=403, detail="you have no rights to delete it")
