import os
from . import create_app
app = create_app('development')

# @app.route("/")
# def hello():
#     return 'hello'
from .category import urls

if __name__ == "__main__":
    app.run()

# from src import app