from flask import request, jsonify
from .. import db
from ..models.ExpenseModel import Expense
from ..models.CateModel import Category
from ..models.SubCateModel import SubCategory
from ..schema.ExpenseSchema import ExpenseSchema, expSchemaMany
from marshmallow import ValidationError

def listExpense():
    # data=Expense.query.all()
    res=[]
    data=db.session.query(Expense, Category.cate_name, SubCategory.sub_cate_name).outerjoin(Category, Expense.cate_id == Category.id).outerjoin(SubCategory, Expense.sub_cate_id == SubCategory.id).all()
    # for y in data:
    #     print("yyyy:", type(y), y)

    for expense, cate_name, sub_cate_name in data:
        serialize = {
            'id': expense.id,
            'amt': expense.amt,
            'desc': expense.desc,
            'cateId': expense.cate_id,
            'subCateId': expense.sub_cate_id,
            'cateName': cate_name,
            'subcateName': sub_cate_name
        }
        res.append(serialize)
    # return{"data:":expSchemaMany.dump(data)},200
    return{"message":res},200


def addExpense():
    data=request.json
    try:
        valid=ExpenseSchema().load(data)
        print("valid:", valid)
        res= Expense(
            cate_id=valid["cate_id"],
            sub_cate_id=valid["sub_cate_id"],
            amt=valid["amt"],
            desc=valid["desc"]
        )
        db.session.add(res)
        db.session.commit()
        return{"message":"Expense added successfully", "data":res}
    except ValidationError as err:
        return {"message":err.messages},422
    

# def deleteExpense(param):
