from flask import Blueprint, request
from flask_restful import Resource, Api 

auth = Blueprint('auth', __name__)

auth_api = Api(auth)





