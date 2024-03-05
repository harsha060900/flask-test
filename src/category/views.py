from flask import request, jsonify
from .. import db
from .models import Category
import uuid

def list_all():
    data= Category.query.all()
    print('data:', data)
    response = []
    for x in data: response.append(x)
    return response

def createCate():
    data = request.form.to_dict()
    res = Category(
        cate_name=data['cate_name']
    )
    db.session.add(res)
    db.session.commit()
    return 'done'
