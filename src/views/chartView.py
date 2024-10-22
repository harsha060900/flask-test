from flask import request, jsonify
from .. import db
import random
import numpy as np
from sqlalchemy import or_
from ..schema.ExpenseSchema import ExpenseSchema, expSchemaMany
from ..models.ExpenseModel import Expense
from ..models.CateModel import Category
from ..models.SubCateModel import SubCategory

generated_colors = set()

def genColors(data=["zero", "one", "two", "three", "four"]):
    while True:
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        if color not in generated_colors:
            generated_colors.add(color)
            return color

def expPieChart():
    data=[]
    start, end, filterBy = request.args.get('start'),request.args.get('end'),request.args.get('filterBy')
    # expData=Expense.query.filter(Expense.type=='expense')
    filterBy = filterBy if filterBy else None
    joinData = db.session.query(Expense, Category.cate_name, SubCategory.sub_cate_name).filter(or_(filterBy is None, Expense.cate_id==filterBy)).join(Category,Expense.cate_id==Category.id).join(SubCategory, Expense.sub_cate_id==SubCategory.id)
    finalData = joinData.filter(Expense.period.between(start, end)).all()
    for expense,cate_name, sub_cate_name in finalData:
        serialize={
            'id': expense.id,
            'expense': expense.amt,
            'period':expense.period,
            'cateId': expense.cate_id,
            'subCateId': expense.sub_cate_id,
            'cateName': cate_name,
            'subCateName': sub_cate_name,
            'bgColor':genColors()
        }
        data.append(serialize)
    return data