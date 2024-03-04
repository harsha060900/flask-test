# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# from .config import config

# db=SQLAlchemy()
# migrate=Migrate()

# def create_app(config_mode):
#     app = Flask(__name__)
#     app.config.from_object(config[config_mode])

#     db.init_app(app)
#     migrate.init_app(app,db)

#     return app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .config import Config

# db = SQLAlchemy()
# migrate = Migrate()

# def create_app(config_mode):
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

    # db.init_app(app)
    # migrate.init_app(app, db)

    # return app