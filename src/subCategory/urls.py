from flask import request
from ..app import app
from .views import list_all_subCate,createSubCate

@app.route("/subCategory", methods=['GET','POST'])
def subCate():
    if request.method=='GET' : return list_all_subCate()
    if request.method=='POST' : return createSubCate()


# @app.route("/subCategory/<cateId>", methods=['GET','PATCH','DELETE'])
# def idCate(cateId):
#     if request.method=='GET' : return list_all(cateId)
#     if request.method=='PATCH' :return updateCate(cateId)
#     if request.method=='DELETE' :return delCate(cateId)
#     else: return 'Method is Not Allowed'