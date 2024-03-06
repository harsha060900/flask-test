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
    data = request.form.to_dict()
    res = Category(
        cate_name=data['cate_name']
    )
    db.session.add(res)
    db.session.commit()
    return 'done'

def updateCate(cateId):
    reqData = request.form
    data = Category.query.get(cateId)
    data.cate_name = reqData['cate_name']
    db.session.commit()
    res = Category.query.get(cateId)
    return jsonify(res)

def delCate(cateId):
    data = Category.query.get(cateId)
    db.session.delete(data)
    db.session.commit()
    return 'Deleted'