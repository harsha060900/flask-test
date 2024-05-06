from marshmallow import fields,Schema
from .. import ma
from .SubCateSchema import SubCateSchema

class CateSchema(Schema):
    id=fields.Int()
    isEdit =fields.Bool()
    isActive =fields.Bool()
    cate_name = fields.Str(required=True)
    sub_cate=fields.Nested(SubCateSchema, many=True)
    # sub_cate=fields.List(fields.Nested(SubCateSchema))

# CateValidate = Schema.from_dict({"cate_name" : fields.Str(required=True)})
cate_sch = CateSchema(many=True)
