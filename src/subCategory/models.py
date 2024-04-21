from datetime import datetime
from dataclasses import dataclass
from .. import db

@dataclass
class SubCategory(db.Model):
    id:int
    sub_cate_name:str
    cate_id:int
    created:datetime
    updated:datetime

    id           = db.Column(db.Integer, primary_key=True )
    created      = db.Column(db.DateTime(timezone=True), default=datetime.now)                           # The Date of the Instance Creation => Created one Time when Instantiation
    updated      = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)    # The Date of the Instance Update => Changed with Every Update

# Input by User Fields:
    sub_cate_name= db.Column(db.String(100), nullable=False, unique=False)
    cate_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    # cate = db.relationship('Category', back_populates="sub_category")