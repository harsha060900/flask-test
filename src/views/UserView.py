from flask import request
from .. import db
from marshmallow import ValidationError
from ..schema.UserSchema import UserSchema,userSchemaMany
from models.UserModel import User 

def addExpense():
    data=request.json
    try:
        valid = UserSchema.load(data)
        res = User(
            user_name=valid['user_name'],
            balance= valid['balance']
        )
    except ValidationError as err:
        return {"message":err.messages},422