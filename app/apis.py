from flask_restful import Api
from app.http_handler.test import *
from app.http_handler.categories import *
from app.http_handler.category_items import *
from app import app

api = Api(app)

api.add_resource(Test, '/test')
api.add_resource(Category, '/categories')
api.add_resource(CategoryItems, '/categories/<int:category_id>')
