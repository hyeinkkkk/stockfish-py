from flask import request
from flask_restful import Resource


class Test(Resource):
    def get(self):
        return {"result":"success"}, 200