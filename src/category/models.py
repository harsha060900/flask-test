from datetime import datetime
from dataclasses import dataclass
from .. import db
from sqlalchemy.orm import validates

@dataclass
class Category(db.Model):
    id:int
    cate_name:str
    isEdit:bool
    isActive:bool
    created:datetime
    updated:datetime

    id           = db.Column(db.Integer, primary_key=True )
    created      = db.Column(db.DateTime(timezone=True), default=datetime.now)                           # The Date of the Instance Creation => Created one Time when Instantiation
    updated      = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)    # The Date of the Instance Update => Changed with Every Update

# Input by User Fields:
    cate_name        = db.Column(db.String(100), nullable=False, unique=False, )
    isEdit =db.Column(db.Boolean, default=False)
    isActive =db.Column(db.Boolean,  default=True)
    sub_cate = db.relationship('SubCategory', backref="category", cascade="all, delete")

    # @validates('cate_name')
    # def validate_cate_name(self, key, value):
    #     if value.isnumeric():
    #         return TypeError("Cate Name must be string")
    #     return value