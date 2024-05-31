from flask import request
from ..app import app
from ..views.expenseView import addExpense,listExpense,deleteExpense,editExpense

@app.route("/expense", methods=['GET','POST'])
def exp():
    if request.method=='GET' : return listExpense()
    if request.method=='POST' : return addExpense()

@app.route("/expense/<paramId>", methods=['DELETE','PUT'])
def expId(paramId):
    if request.method=='DELETE' : return deleteExpense(paramId)
    if request.method=='PUT' : return editExpense(paramId)

