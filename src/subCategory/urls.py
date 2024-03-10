from flask import request
from ..app import app
from .views import list_all_subCate,createSubCate,updateSubCate,delSubCate

@app.route("/subCategory", methods=['GET','POST'])
def subCate():
    if request.method=='GET' : return list_all_subCate()
    if request.method=='POST' : return createSubCate()


@app.route("/subCategory/<paramId>", methods=['GET','PATCH','DELETE'])
def subIdCate(paramId):
    if request.method=='GET' : return list_all_subCate(paramId)
    if request.method=='PATCH' :return updateSubCate(paramId)
    if request.method=='DELETE' :return delSubCate(paramId)
    else: return 'Method is Not Allowed'