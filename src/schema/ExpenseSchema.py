from marshmallow import fields,Schema
from .CateSchema import cateSchemaMany, cateSchema

class ExpenseSchema(Schema):
    id=fields.Int()
    cate_id=fields.Int(allow_none=True)
    sub_cate_id=fields.Int(allow_none=True)
    amt=fields.Float(required=True)
    period=fields.DateTime(required=True)
    desc=fields.Str(allow_none=True)
    type=fields.Str()

expSchemaMany = ExpenseSchema(many=True)