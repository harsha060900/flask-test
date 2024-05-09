from marshmallow import fields,Schema

class ExpenseSchema(Schema):
    id=fields.Int()
    cate_id=fields.Int(required=True)
    sub_cate_id=fields.Int(allow_none=True)
    amt=fields.Float(required=True)
    desc=fields.Str(allow_none=True, missing=None)

expSchemaMany = ExpenseSchema(many=True)