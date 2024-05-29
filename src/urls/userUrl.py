from flask import request
from ..app import app
from ..models.UserModel import User

@app.route("/user", methods=['GET','POST'])
def user():
    pass
    if request.method=='GET' : return User.query.all() 
    # if request.method=='POST' : return addExpense()