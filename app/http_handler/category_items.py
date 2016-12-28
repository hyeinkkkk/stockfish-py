from flask import request
from flask_restful import Resource
from ..models import items


class CategoryItems(Resource):
    def get(self, category_id):
        return items.get_list_by_category(category_id), 200