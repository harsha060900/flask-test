from flask import request
from ..app import app
from ..views.expenseView import addExpense,listExpense

@app.route("/expense", methods=['GET','POST'])
def exp():
    if request.method=='GET' : return listExpense()
    if request.method=='POST' : return addExpense()