from datetime import datetime
from dataclasses import dataclass
from .. import db

@dataclass
class User(db.Model):
    id:int
    user_name:str
    balance:float
    created:datetime
    updated:datetime

    id = db.Column(db.Integer, primary_key=True)
    user_name=db.Column(db.String(100))
    balance=db.Column(db.Float)
    created      = db.Column(db.DateTime(timezone=True), default=datetime.now)                           # The Date of the Instance Creation => Created one Time when Instantiation
    updated      = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)    # The Date of the Instance Update => Changed with Every Update