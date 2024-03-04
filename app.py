# import os
# from . import create_app
# app = create_app(os.getenv("DATABASE_URL"))

# @app.route("/")
# def hello():
#     return 'hello'

# if __name__ == "__main__":
#     app.run()

from src import app
# App Initialization
# from . import create_app # from __init__ file
# app = create_app(os.getenv("CONFIG_MODE"))

# Hello World!
# @app.route('/')
# def hello():
#     return "Hello World!"

# if __name__ == "__main__":
#     app.run()