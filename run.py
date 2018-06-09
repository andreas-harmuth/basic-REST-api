from flask import Flask
from flask_cors import CORS
import sys



def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from app import api_bp
    app.register_blueprint(api_bp)

    from models import db, bcrypt
    db.init_app(app)
    bcrypt.init_app(app)

    CORS(app, resources=app.config['CORS_RESOURCES'])

    return app

# Create the application
application = create_app("config_dev")