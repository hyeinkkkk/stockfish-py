from flask import request
from flask_restful import Resource
from ..models import categories


class Category(Resource):
    def get(self):
        return categories.get_all(), 200