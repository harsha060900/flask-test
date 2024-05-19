from marshmallow import fields,Schema
from .CateSchema import cateSchemaMany, cateSchema

class ExpenseSchema(Schema):
    id=fields.Int()
    cate_id=fields.Int(required=True)
    sub_cate_id=fields.Int(allow_none=True)
    amt=fields.Float(required=True)
    period=fields.DateTime(required=False)
    desc=fields.Str(allow_none=True)

expSchemaMany = ExpenseSchema(many=True)