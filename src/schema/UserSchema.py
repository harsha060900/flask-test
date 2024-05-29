from marshmallow import fields,Schema

class UserSchema(Schema):
    id=fields.Int()
    user_name=fields.String(allow_none=True)
    balance =fields.Float(allow_none=True)

userSchemaMany = UserSchema(many=True)