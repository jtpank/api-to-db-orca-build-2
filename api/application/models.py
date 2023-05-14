from . import db
from flask_restful import reqparse, abort, Api, Resource, fields, marshal_with
import json
#sports
# "key":"americanfootball_ncaaf"
#"americanfootball_nfl"
#"basketball_nba"
#User and Schema
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    email = db.Column(db.String(30), unique=True)

    def __repr__(self):
        return '<USERS {}>'.format(self.username)
    def __init__(self, username, email, password):
        self.username =     username
        self.email =        email

class UserSchema():
    resource_fields = {
        "id": fields.Integer,
        "username": fields.String,
        "email": fields.String,
    }
    args_field = reqparse.RequestParser()
    args_field.add_argument("username", type=str,help="username is required", required=True)
    args_field.add_argument("email", type=str,help="email is required", required=True)
