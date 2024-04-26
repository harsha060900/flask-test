from flask import request, jsonify
from .. import db
from .models import Category
import uuid
from sqlalchemy import exc
from ..schema.validators import CateValidate
from marshmallow import ValidationError

def list_all(cateId=None):
    if not cateId:
        data= Category.query.all()
        print('data:',jsonify(data))
    else:
        data = Category.query.get(cateId)
    return jsonify(data)

def createCate():
    data = request.json
    print('input:',data)
    try:
        valid=CateValidate().load(data)
        res = Category(
        cate_name=valid['cate_name'],
    )
        db.session.add(res)
        db.session.commit()
        return {"message":"Category created successfully"}
    except ValidationError as err:
        print('error:',err)
        return {"message":err.messages},422
    # try:
    #     db.session.add(res)
    #     db.session.commit()
    #     return {"message":"Category created successfully"}
    # except exc.SQLAlchemyError as e :
    #     db.session.rollback()
    #     print('sqlerror:',AssertionError.__init__)
    #     return jsonify(msg='Error: {}. '.format(e.__class__)), 422

def updateCate(cateId):
    reqData = request.json
    data = Category.query.get(cateId)
    if not data:
        return {"message":"No records found"}
    # for key,val in reqData.items(): 
    #     print('aa:', data[key], key, val)
    #     data[key] = val 
    data.cate_name = reqData['cate_name']
    db.session.commit()
    res = Category.query.get(cateId)
    return jsonify(res)

def delCate(cateId):
    data = Category.query.get(cateId)
    db.session.delete(data)
    db.session.commit()
    return 'Deleted'