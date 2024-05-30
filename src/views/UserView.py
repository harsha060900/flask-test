from flask import request
from .. import db
from marshmallow import ValidationError
from ..schema.UserSchema import UserSchema,userSchemaMany
from ..models.UserModel import User 

def listUser():
    data=User.query.all()
    if data:
        return{"data":userSchemaMany.dump(data)}
    return{"message":"No record found"}

def addBalance():
    data=request.json
    try:
        valid = UserSchema().load(data)
        res = User(
            user_name=valid['user_name'],
            balance= valid['balance']
        )
        db.session.add(res)
        db.session.commit()
        return{"message":"Balance added successfully","data:":res},200
    except ValidationError as err:
        return {"message":err.messages},422