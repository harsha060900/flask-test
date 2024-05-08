from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS

from .config import config

db = SQLAlchemy()
migrate= Migrate()
ma=Marshmallow()

def create_app(config_mode):
    app = Flask(__name__)
    app.config.from_object(config[config_mode])
    CORS(app)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app,db)
    # db = SQLAlchemy(app)
    # migrate = Migrate(app, db)
    return app