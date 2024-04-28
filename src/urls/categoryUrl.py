from flask import request
from ..app import app
from ..views.CateView import list_all, updateCate,createCate,delCate

@app.route("/category", methods=['GET','POST'])
def cate():
    if request.method=='GET' : return list_all()
    if request.method=='POST' : return createCate()


@app.route("/category/<cateId>", methods=['GET','PATCH','DELETE'])
def idCate(cateId):
    if request.method=='GET' : return list_all(cateId)
    if request.method=='PATCH' :return updateCate(cateId)
    if request.method=='DELETE' :return delCate(cateId)
    else: return 'Method is Not Allowed'