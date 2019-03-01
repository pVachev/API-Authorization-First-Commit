from flask import Flask, request
from flask_restful import Resource, Api
from api import 3_auth
from 3_auth import auth


app = Flask(__name__)
api = Api(app)

class Item(Resource):
    def get(self, name):
        return {"Hello, " + 'item': name}

api.add_resource(Item, '/item/<string:name>')




