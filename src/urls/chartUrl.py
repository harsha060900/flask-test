from flask import request
from ..app import app
from ..views.chartView import expPieChart

@app.route("/pie-chart", methods=['GET','POST'])
def pieChart():
    if request.method=='GET' : return expPieChart()