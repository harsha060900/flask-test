from flask import request
from ..app import app
from .views import list_all, createCate

@app.route("/getList")
def listCate():
    if request.method=='GET' : return list_all()

@app.route("/addCate", methods=['POST'])
def addCate():
    return createCate()