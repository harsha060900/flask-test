import os
from . import create_app
app = create_app('development')

# @app.route("/")
# def hello():
#     return 'hello'
# from .category import urls
from .urls import subCateUrl
from .urls import categoryUrl
from .urls import expenseUrl

@app.errorhandler(422)
def internal_server_error(e):
    return "INternal error",422

@app.errorhandler(404)
def resource_not_found(e):
    return "Route not found", 404

if __name__ == "__main__":
    app.run()

# from src import app