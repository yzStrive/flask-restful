
from flask import jsonify
from flask_restful import Resource
import uuid
class Admin(Resource):
    def get(self):
        return jsonify({'id':uuid.uuid4()})