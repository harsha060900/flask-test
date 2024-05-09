from flask import request, jsonify
from .. import db
from ..models.ExpenseModel import Expense
from ..schema.ExpenseSchema import ExpenseSchema, expSchemaMany
from marshmallow import ValidationError

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