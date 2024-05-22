from flask import request, jsonify
from .. import db
from ..models.ExpenseModel import Expense
from ..models.CateModel import Category
from ..models.SubCateModel import SubCategory
from ..schema.ExpenseSchema import ExpenseSchema, expSchemaMany
from marshmallow import ValidationError
from datetime import datetime

def listExpense():
    orderBy=request.args.get('orderBy')
    res=[]
    if orderBy == "desc":
        data=db.session.query(Expense, Category.cate_name, SubCategory.sub_cate_name).outerjoin(Category, Expense.cate_id == Category.id).outerjoin(SubCategory, Expense.sub_cate_id == SubCategory.id).order_by(Expense.created.desc()).all()
    else:
        data=db.session.query(Expense, Category.cate_name, SubCategory.sub_cate_name).outerjoin(Category, Expense.cate_id == Category.id).outerjoin(SubCategory, Expense.sub_cate_id == SubCategory.id).order_by(Expense.created.asc()).all()
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
        print("valid:", valid)
        res= Expense(
            cate_id=valid["cate_id"],
            sub_cate_id=valid["sub_cate_id"],
            amt=valid["amt"],
            period=valid["period"],
            desc=valid["desc"]
        )
        db.session.add(res)
        db.session.commit()
        return{"message":"Expense added successfully", "data":res}
    except ValidationError as err:
        return {"message":err.messages},422
    
def deleteExpense(paramId):
    data= Expense.query.get(paramId)
    if not data:
        return {"message":"No records found"},200
    db.session.delete(data)
    db.session.commit()
    return {"message":"Expense deleted successfully","data":data},200
