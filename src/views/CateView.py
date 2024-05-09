from flask import request, jsonify
from .. import db
from ..models.CateModel import Category
from marshmallow import ValidationError
from ..schema.CateSchema import cateSchema,cateSchemaMany

def list_all(cateId=None):
    args=request.args.get('search')
    if request.args:
        search=Category.query.filter(Category.cate_name.ilike('%'+args.lower()+'%')).all()
        return {"data":cateSchemaMany.dump(search)}
    # if not cateId:
    #     data = Category.query.all()
        # data= db.session.query(Category,SubCategory).outerjoin(SubCategory, Category.id==SubCategory.cate_id).all()
        # print('aa:',db.session.query(Category,SubCategory).outerjoin(SubCategory, Category.id==SubCategory.cate_id).all())
    else:
        data = Category.query.get(cateId)
    return {"data":cateSchemaMany.dump(data)}
    # return jsonify(data1),200

def createCate():
    data = request.json
    try:
        valid=cateSchema.load(data)
        res = Category(
        cate_name=valid['cate_name'],
    )
        db.session.add(res)
        db.session.commit()
        return {"message":"Category created successfully"}
    except ValidationError as err:
        return {"message":err.messages},422

def updateCate(cateId):
    reqData = request.json
    dbData = Category.query.get(cateId)
    if not dbData:
        return {"message":"No records found"},200
    # for key,val in reqData.items(): 
    #     print('aa:', data[key], key, val)
    #     data[key] = val 
    try:
        valid=cateSchema.load(reqData)
        dbData.cate_name = valid['cate_name']
        db.session.commit()
        return {"message":"Category updated successfully","data":dbData},200
    except ValidationError as err:
        return {"message":err.messages},422

def delCate(cateId):
    data = Category.query.get(cateId)
    if not data:
        return {"message":"No records found"},200
    db.session.delete(data)
    db.session.commit()
    return {"message":"Category deleted successfully","data":data},200