from flask import request
from ..app import app
from ..views.expenseView import addExpense,listExpense,deleteExpense

@app.route("/expense", methods=['GET','POST'])
def exp():
    if request.method=='GET' : return listExpense()
    if request.method=='POST' : return addExpense()

@app.route("/expense/<paramId>", methods=['DELETE','PATCH'])
def expId(paramId):
    if request.method=='DELETE' : return deleteExpense(paramId)
    # if request.method=='POST' : return addExpense()

