from marshmallow import fields,Schema
from .CateSchema import cateSchemaMany, cateSchema

class ExpenseSchema(Schema):
    id=fields.Int()
    cate_id=fields.Int(allow_none=True, load_default=None)
    sub_cate_id=fields.Int(allow_none=True, load_default=None)
    amt=fields.Float(required=True)
    period=fields.DateTime(required=True)
    desc=fields.Str(allow_none=True, load_default=None)
    type=fields.Str()

expSchemaMany = ExpenseSchema(many=True)