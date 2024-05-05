from marshmallow import fields,Schema
from .SubCateSchema import SubCateSchema
from .. import ma

class CateSchema(ma.Schema):
    cate_name = fields.Str(required=True)

class CateSerialize():
    sub_cate=fields.Nested(SubCateSchema, many=True)
# CateValidate = Schema.from_dict({"cate_name" : fields.Str(required=True)})