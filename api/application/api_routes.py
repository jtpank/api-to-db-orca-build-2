
from flask import flash, Flask, request, jsonify, render_template, redirect, url_for, session, Blueprint, make_response, json
from flask_jwt_extended import get_jwt_identity, jwt_required, JWTManager
from flask_restful import reqparse, abort, Api, Resource, fields, marshal_with
from flask import current_app, Blueprint, send_file, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc, and_, distinct, or_
from .models import db
api_main = Blueprint('api', __name__, template_folder='templates')
api = Api(api_main)
app = current_app


#auxiliary functions

# end auxiliary functions

#404 response if field not existent
def abort_if_field_not_exist(data_field, data):
    if data_field not in data:
        abort(404, message="error_message_field: {} does not exist".format(data_field))
#404 response if field not existent
def abort_if_none(data, _id):
    if data is None:
        abort(404, error_message_field="Field: {} does not exist".format(_id))
def abort_if_table_none(data):
    if data is None:
        abort(404, error_message_field="Field: table does not exist")

#User login and sign up routes + protected route example:
class live_nba_odds_data(Resource):
    def get(self):
        data = {'message': "live_nba_odds_data get route"}
        return data, 200
    def put(self):
        try:
            data =  {
                "message": "return message",
                }
            return data, 200
        except Exception as e:
            return {'message': 'Failed to put live_nba_odds_data data: {}'.format(str(e))}, 500


class index_class(Resource):
    def get(self):
        return {"api-for-dk" : "index_page"}
#add resources
api.add_resource(index_class, '/api')
api.add_resource(index_class, '/api/live_nba_odds_data')