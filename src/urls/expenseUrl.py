from flask import request
from ..app import app
from ..views.expenseView import addExpense

@app.route("/expense", methods=['GET','POST'])
def exp():
    pass
    if request.method=='POST' : return addExpense()