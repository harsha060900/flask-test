from marshmallow import Schema, fields

class SubCateSchema(Schema):
    cate_id =fields.Int(required=True)
    sub_cate_name = fields.Str(required=True)