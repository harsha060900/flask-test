from flask import request, jsonify
from .. import db
from ..models.SubCateModel import SubCategory
from ..schema.SubCateSchema import SubCateSchema, subCateSchemaMany
from marshmallow import ValidationError

def list_all_subCate(paramId=None):
    args=request.args.get('cate_id')
    print('a:',args)
    if args:
        data = SubCategory.query.filter(SubCategory.cate_id==args)
    elif not paramId:
        data= SubCategory.query.all()
    else:
        data = SubCategory.query.get(paramId)
    if data:
        return {"data":subCateSchemaMany.dump(data)}
    else: return{"message":"No record found"}

def createSubCate():
    reqData = request.json
    try:
        valid= SubCateSchema().load(reqData)
        res=SubCategory(
            sub_cate_name = valid['sub_cate_name'],
            cate_id =valid["cate_id"]
        )
        db.session.add(res)
        db.session.commit()
        return{"message":"Subcategory created successfully","data:":res},200
    except ValidationError as err:
        return{'message':err.messages},422

def updateSubCate(paramId):
    reqData = request.json
    data = SubCategory.query.get(paramId)
    if not data:
        return {"message":"No records found"}
    # for key,val in reqData.items(): 
    #     print('aa:', data[key], key, val)
    #     data[key] = val 
    data.sub_cate_name = reqData['sub_cate_name']
    data.cate_id = reqData['cate_id']
    db.session.commit()
    res = SubCategory.query.get(paramId)
    return {"data":res,"message":"Subcategory updated successfully"}

def delSubCate(paramId):
    data = SubCategory.query.get(paramId)
    if not data:
        return {"message":"No records found"}
    db.session.delete(data)
    db.session.commit()
    return {"data":data,"message":"Subcategory deleted successfully"},200