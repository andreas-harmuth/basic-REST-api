from flask import Blueprint
from flask_restful import Api

api_bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_bp)


"""
Resources
from resources.file import Class

api.add_resource(Class, '/route')
"""
