import os

ENV = "development"
DEBUG = True
PORT = 6300
APP_NAME = "spectracular"



# SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "sqlite:///"+APP_NAME+".db"


# JWT
# JWT_SECRET_KEY = 'dxctke2NbddypG5B'


# CORS
# TODO: add list of available origins
CORS_RESOURCES = {r"/api/*": {"origins": "*"}}


# Images
# UPLOAD_FOLDER = './static/images'
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
# MAX_CONTENT_LENGTH = 16*1024*1024  #16 mb
