from flask import request, jsonify
from .. import db
from .models import SubCategory
from ..category.models import Category
import uuid

def list_all_subCate(paramId=None):
    if not paramId:
        data= SubCategory.query.all()
    else:
        data = SubCategory.query.get(paramId)
    if data:
        return jsonify(data)
    else: return{"message":"No record found"}

def createSubCate():
    reqData = request.json
    cateData = Category.query.get(reqData['cate_id'])
    if not cateData:
        return{"message":"Select a category"}
    resSubCate=SubCategory(
        sub_cate_name = reqData['sub_cate_name'],
        cate_id =reqData["cate_id"]
    )
    db.session.add(resSubCate)
    db.session.commit()
    return{"message":"Subcategory created successfully"}

def updateSubCate(paramId):
    reqData = request.json
    data = SubCategory.query.get(paramId)
    if not data:
        return {"message":"No records found"}
    # for key,val in reqData.items(): 
    #     print('aa:', data[key], key, val)
    #     data[key] = val 
    data.sub_cate_name = reqData['cate_name']
    data.cate_id = reqData['cate_id']
    db.session.commit()
    res = SubCategory.query.get(paramId)
    return {"data":res,"message":"Updated successfully"}

def delSubCate(paramId):
    data = SubCategory.query.get(paramId)
    db.session.delete(data)
    db.session.commit()
    return 'Deleted'