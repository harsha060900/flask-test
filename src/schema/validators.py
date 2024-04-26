from marshmallow import Schema, fields

class CateValidate(Schema):
    cate_name = fields.Str(required=True)

# CateValidate = Schema.from_dict({"cate_name" : fields.Str(required=True)})