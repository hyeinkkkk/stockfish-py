from flask_restful import Api
from app.http_handler.test import *
from app import app

api = Api(app)

api.add_resource(Test, '/test')