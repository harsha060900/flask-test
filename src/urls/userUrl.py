from flask import request
from ..app import app
from ..models.UserModel import User
from ..views.UserView import listUser, addBalance

@app.route("/user", methods=['GET','POST'])
def user():
    pass
    if request.method=='GET' : return listUser() 
    if request.method=='POST' : return addBalance()