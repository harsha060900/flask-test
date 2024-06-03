from flask import request, jsonify
from .. import db
from ..models.ExpenseModel import Expense
from ..models.CateModel import Category
from ..models.SubCateModel import SubCategory
from ..schema.ExpenseSchema import ExpenseSchema, expSchemaMany
from marshmallow import ValidationError
from datetime import datetime

# code from AI for between
# python
# from sqlalchemy import and_, or_

# start_date = request.args.get('start_date')
# end_date = request.args.get('end_date')

# query = db.session.query(Expense, Category.cate_name, SubCategory.sub_cate_name)
# query = query.outerjoin(Category, Expense.cate_id == Category.id)
# query = query.outerjoin(SubCategory, Expense.sub_cate_id == SubCategory.id)
# query = query.order_by(Expense.created.asc())

# if start_date and end_date:
#     query = query.filter(Expense.period.between(start_date, end_date))

# data = query.all()

def listExpense():
    orderBy=request.args.get('orderBy')
    start,end=request.args.get('start'),request.args.get('end')
    res=[]
    data=data=db.session.query(Expense, Category.cate_name, SubCategory.sub_cate_name).outerjoin(Category, Expense.cate_id == Category.id).outerjoin(SubCategory, Expense.sub_cate_id == SubCategory.id)
    if orderBy == "asc" and not end:
        data=data.order_by(Expense.created.asc()).all()
    elif start and end:
        print('ssss:',start,end)
        data=data.filter(Expense.period.between(start,end)).order_by(Expense.created.desc()).all()
    else:
        data=data.order_by(Expense.created.desc()).all()
    for expense, cate_name, sub_cate_name in data:
        serialize = {
            'id': expense.id,
            'amt': expense.amt,
            'period':expense.period,
            'desc': expense.desc,
            'cateId': expense.cate_id,
            'subCateId': expense.sub_cate_id,
            'cateName': cate_name,
            'subCateName': sub_cate_name,
            'type':expense.type,
            'created':expense.created
        }
        res.append(serialize)
    # return{"data:":expSchemaMany.dump(data)},200
    return{"data":res},200

def addExpense():
    data=request.json
    # start_time = datetime.strptime(data["period"], '%Y-%m-%d %H:%M:%S')
    # print('ss:',start_time)
    try:
        valid=ExpenseSchema().load(data)
        res= Expense(
            cate_id=valid["cate_id"],
            sub_cate_id=valid["sub_cate_id"],
            amt=valid["amt"],
            period=valid["period"],
            desc=valid["desc"],
            type=valid["type"]
        )
        db.session.add(res)
        db.session.commit()
        return{"message":"Expense added successfully", "data":res}
    except ValidationError as err:
        return {"message":err.messages},422

def editExpense(paramId):
    reqData=request.json
    data=Expense.query.get(paramId)
    # start_time = datetime.strptime(data["period"], '%Y-%m-%d %H:%M:%S')
    # print('ss:',start_time)
    try:
        valid=ExpenseSchema().load(reqData)
        data.cate_id=valid["cate_id"],
        data.sub_cate_id=valid["sub_cate_id"],
        data.amt=valid["amt"],
        data.period=valid["period"],
        data.desc=valid["desc"]
        db.session.commit()
        return{"message":"Expense updated successfully", "data":data}
    except ValidationError as err:
        return {"message":err.messages},422
    
def deleteExpense(paramId):
    data= Expense.query.get(paramId)
    if not data:
        return {"message":"No records found"},200
    db.session.delete(data)
    db.session.commit()
    return {"message":"Expense deleted successfully","data":data},200
