from datetime import datetime
from dataclasses import dataclass
from .. import db

@dataclass
class Category(db.Model):
    id:int
    cate_name:str
    created:datetime
    updated:datetime

    id           = db.Column(db.Integer, primary_key=True )
    created      = db.Column(db.DateTime(timezone=True), default=datetime.now)                           # The Date of the Instance Creation => Created one Time when Instantiation
    updated      = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)    # The Date of the Instance Update => Changed with Every Update

# Input by User Fields:
    cate_name        = db.Column(db.String(100), nullable=False, unique=False)