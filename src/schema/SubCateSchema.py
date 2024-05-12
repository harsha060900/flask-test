from marshmallow import Schema, fields

class SubCateSchema(Schema):
    id=fields.Int()
    isEdit =fields.Bool()
    isActive =fields.Bool()
    cate_id =fields.Int(required=True)
    sub_cate_name = fields.Str(required=True)

subCateSchemaMany = SubCateSchema(many=True)