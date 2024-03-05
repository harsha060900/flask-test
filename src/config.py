import os
# class DevelopmentConfig():
#     DEVELOPMENT = True
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    
# config={
#     "development":DevelopmentConfig
# }

class DevConfig(object):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

config={
    "development":DevConfig
}