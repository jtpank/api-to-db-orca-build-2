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


#Base sport template example
class LiveNbaData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    odds_api_game_id = db.Column(db.String(32), unique=True)
    sport_key = db.Column(db.String(25))
    commence_time = db.Column(db.DateTime)
    home_team = db.Column(db.String(23))
    away_team = db.Column(db.String(23))
    home_team_score = db.Column(db.Integer)
    away_team_score = db.Column(db.Integer)
    completed = db.Column(db.Integer)

class LiveNbaDataSchema():
    resource_fields = {
        "id": fields.Integer,
        "odds_api_game_id": fields.String,
        "sport_key": fields.String,
        "commence_time": fields.DateTime,
        "home_team": fields.String,
        "away_team": fields.String,
        "home_team_score": fields.Integer,
        "away_team_score": fields.Integer,
        "completed": fields.Integer,
    }
    args_field = reqparse.RequestParser()
    args_field.add_argument("sport_key", type=str,help="sport_key is required", required=True)
    args_field.add_argument("odds_api_game_id", type=str,help="odds_api_game_id is required", required=True)

#Base bookmaker schema with last update time field to be unique
class Bookmaker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    odds_api_game_id = db.Column(db.String(32))
    sport_key = db.Column(db.String(25))
    odds_api_bookmaker_key = db.Column(db.String(30))
    odds_api_bookmaker_title = db.Column(db.String(30))
    commence_time = db.Column(db.DateTime)
    last_update = db.Column(db.String(20))

class BookmakerSchema():
    resource_fields = {
        "id": fields.Integer,
        "odds_api_game_id": fields.String,
        "sport_key": fields.String,
        "odds_api_bookmaker_key": fields.String,
        "odds_api_bookmaker_title": fields.String,
        "commence_time": fields.DateTime,
        "last_update": fields.String,
    }
    args_field = reqparse.RequestParser()
    args_field.add_argument("sport_key", type=str,help="sport_key is required", required=True)
    args_field.add_argument("odds_api_game_id", type=str,help="odds_api_game_id is required", required=True)
    args_field.add_argument("odds_api_bookmaker_key", type=str,help="odds_api_bookmaker_key is required", required=True)
    args_field.add_argument("odds_api_bookmaker_title", type=str,help="odds_api_bookmaker_title is required", required=True)
    args_field.add_argument("last_update", type=str,help="last_update is required", required=True)

class MoneylineMarket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    odds_api_game_id = db.Column(db.String(32))
    sport_key = db.Column(db.String(25))
    odds_api_bookmaker_key = db.Column(db.String(30))
    commence_time = db.Column(db.DateTime)
    last_update = db.Column(db.String(20))
    home_team = db.Column(db.String(23))
    away_team = db.Column(db.String(23))
    home_team_price = db.Column(db.Integer)  
    away_team_price = db.Column(db.Integer)
class MoneylineMarketSchema():
    resource_fields = {
        "id": fields.Integer,
        "odds_api_game_id": fields.String,
        "sport_key": fields.String,
        "odds_api_bookmaker_key": fields.String,
        "commence_time": fields.DateTime,
        "last_update": fields.String,
        "home_team": fields.String,
        "away_team": fields.String,
        "home_team_price": fields.Integer,
        "away_team_price": fields.Integer,
    }
    args_field = reqparse.RequestParser()
    args_field.add_argument("sport_key", type=str,help="sport_key is required", required=True)
    args_field.add_argument("odds_api_game_id", type=str,help="odds_api_game_id is required", required=True)
    args_field.add_argument("last_update", type=str,help="last_update is required", required=True)
    
class SpreadMarket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    odds_api_game_id = db.Column(db.String(32))
    sport_key = db.Column(db.String(25))
    odds_api_bookmaker_key = db.Column(db.String(30))
    commence_time = db.Column(db.DateTime)
    last_update = db.Column(db.String(20))
    home_team = db.Column(db.String(23))
    away_team = db.Column(db.String(23))
    home_team_price = db.Column(db.Integer)  
    away_team_price = db.Column(db.Integer)
    home_team_points = db.Column(db.Integer)  
    away_team_points = db.Column(db.Integer)
class SpreadMarketSchema():
    resource_fields = {
        "id": fields.Integer,
        "odds_api_game_id": fields.String,
        "sport_key": fields.String,
        "odds_api_bookmaker_key": fields.String,
        "commence_time": fields.DateTime,
        "last_update": fields.String,
        "home_team": fields.String,
        "away_team": fields.String,
        "home_team_price": fields.Integer,
        "away_team_price": fields.Integer,
        "home_team_points": fields.Integer,
        "away_team_points": fields.Integer,
    }
    args_field = reqparse.RequestParser()
    args_field.add_argument("sport_key", type=str,help="sport_key is required", required=True)
    args_field.add_argument("odds_api_game_id", type=str,help="odds_api_game_id is required", required=True)
    args_field.add_argument("last_update", type=str,help="last_update is required", required=True)

class TotalsMarket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    odds_api_game_id = db.Column(db.String(32))
    sport_key = db.Column(db.String(25))
    odds_api_bookmaker_key = db.Column(db.String(30))
    commence_time = db.Column(db.DateTime)
    last_update = db.Column(db.String(20))
    over_price = db.Column(db.Integer)  
    under_price = db.Column(db.Integer)
    over_points = db.Column(db.Integer)  
    under_points = db.Column(db.Integer)
class TotalsMarketSchema():
    resource_fields = {
        "id": fields.Integer,
        "odds_api_game_id": fields.String,
        "sport_key": fields.String,
        "odds_api_bookmaker_key": fields.String,
        "commence_time": fields.DateTime,
        "last_update": fields.String,
        "over_price": fields.Integer,
        "under_price": fields.Integer,
        "over_points": fields.Integer,
        "under_points": fields.Integer,
    }
    args_field = reqparse.RequestParser()
    args_field.add_argument("sport_key", type=str,help="sport_key is required", required=True)
    args_field.add_argument("odds_api_game_id", type=str,help="odds_api_game_id is required", required=True)
    args_field.add_argument("last_update", type=str,help="last_update is required", required=True)