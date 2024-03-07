from flask import request, jsonify
from .. import db
from .models import Category
import uuid

def list_all(cateId=None):
    if not cateId:
        data= Category.query.all()
    else:
        data = Category.query.get(cateId)
    return jsonify(data)

def createCate():
    data = request.json
    res = Category(
        cate_name=data['cate_name'],
        cost=data['cost']
    )
    db.session.add(res)
    db.session.commit()
    return {"message":"Category created successfully"}

def updateCate(cateId):
    reqData = request.json
    data = Category.query.get(cateId)
    if not data:
        return {"message":"No records found"}
    # for key,val in reqData.items(): 
    #     print('aa:', data[key], key, val)
    #     data[key] = val 
    data.cate_name = reqData['cate_name']
    data.cost = reqData['cost']
    db.session.commit()
    res = Category.query.get(cateId)
    return jsonify(res)

def delCate(cateId):
    data = Category.query.get(cateId)
    db.session.delete(data)
    db.session.commit()
    return 'Deleted'