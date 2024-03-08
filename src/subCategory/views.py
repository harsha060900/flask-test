from flask import request, jsonify
from .. import db
from .models import SubCategory
import uuid

def list_all_subCate(cateId=None):
    if not cateId:
        data= SubCategory.query.all()
    else:
        data = SubCategory.query.get(cateId)
    return jsonify(data)

def createSubCate():
    reqData = request.json
    res=SubCategory(
        sub_cate_name = reqData['sub_cate_name'],
        cost=reqData["cost"],
        cate_id = reqData['cate_id']
    )
    db.session.add(res)
    db.session.commit()
    return{"message:","Subcategory created successfully"}