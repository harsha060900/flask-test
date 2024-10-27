from flask import request, jsonify
from .. import db
import random
import numpy as np
from sqlalchemy import func
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
    res={'data':[], 'totExp':0}
    start, end, filterBy = request.args.get('start'),request.args.get('end'),request.args.get('filterBy')
    # expData=Expense.query.filter(Expense.type=='expense')
    filterBy = filterBy if filterBy else None
    allCateData=None
    periodData = Expense.query.filter(Expense.period.between(start, end), or_(filterBy is None, Expense.cate_id==filterBy)).subquery()
    if filterBy:
        allCateData = db.session.query(periodData.c.sub_cate_id, SubCategory.sub_cate_name, func.sum(periodData.c.amt).label('amt')).join(SubCategory, periodData.c.sub_cate_id == SubCategory.id).group_by(periodData.c.sub_cate_id,SubCategory.sub_cate_name)
        print("A:",allCateData.all())
    else:
        allCateData = db.session.query(periodData.c.cate_id, Category.cate_name,func.sum(periodData.c.amt).label('amt')).join(Category, periodData.c.cate_id == Category.id).group_by(periodData.c.cate_id, Category.cate_name).all()
    # joinData = db.session.query(Expense.cate_id, Category.cate_name, func.sum(Expense.amt)).filter(or_(filterBy is None, Expense.cate_id==filterBy)).join(Category,Expense.cate_id==Category.id).join(SubCategory, Expense.sub_cate_id==SubCategory.id).group_by(Expense.cate_id, Category.cate_name)
    for cate_id,cate_name,  tot in allCateData:
        serialize={
            # 'expense': expense.amt,
            'expense': tot,
            'cateId': cate_id,
            'cateName': cate_name,
            'bgColor':genColors()
        }
        res['data'].append(serialize)
        res["totExp"]+=tot
    return res