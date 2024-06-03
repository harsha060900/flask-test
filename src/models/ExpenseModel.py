from datetime import datetime
from dataclasses import dataclass
from .. import db

@dataclass
class Expense(db.Model):
    id:int
    created:datetime
    updated:datetime
    cate_id:int
    sub_cate_id:int
    amt:float
    period:datetime
    desc:str

    id           = db.Column(db.Integer, primary_key=True )
    created      = db.Column(db.DateTime(timezone=True), default=datetime.now)                           # The Date of the Instance Creation => Created one Time when Instantiation
    updated      = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)    # The Date of the Instance Update => Changed with Every Update

# Input by User
    cate_id=db.Column(db.Integer, db.ForeignKey("category.id"))
    sub_cate_id=db.Column(db.Integer, db.ForeignKey("sub_category.id"))
    amt=db.Column(db.Float, nullable=False)
    period=db.Column(db.DateTime(timezone=True), nullable=False)
    desc=db.Column(db.Text)
    type=db.Column(db.String)