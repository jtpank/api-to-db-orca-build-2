
from flask import flash, Flask, request, jsonify, render_template, redirect, url_for, session, Blueprint, make_response, json
from flask_jwt_extended import get_jwt_identity, jwt_required, JWTManager
from flask_restful import reqparse, abort, Api, Resource, fields, marshal_with
from flask import current_app, Blueprint, send_file, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc, and_, distinct, or_
from .models import db, SpreadMarket, SpreadMarketSchema, Bookmaker, BookmakerSchema
from dotenv import load_dotenv
import requests
import os
load_dotenv()
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




#example get request for scores for nba
#https://api.the-odds-api.com/v4/sports/basketball_nba/scores?apiKey=f2c87d0ea0ee1e114c5e603c9693aa7b&dateFormat=iso&date=2023-05-17T00:00:00Z
#[
# {"id":"c416e8cf41fbdb4848e9a71809b58ef8",
# "sport_key":"basketball_nba",
# "sport_title":"NBA",
# "commence_time":"2023-05-18T00:30:00Z",
# "completed":true,
# "home_team":"Boston Celtics",
# "away_team":"Miami Heat",
# "scores":[
# {"name":"Boston Celtics","score":"112"},
# {"name":"Philadelphia 76ers","score":"88"}
# ],
# "last_update":"2023-05-15T03:33:07Z"},
# {"id":"d154a9750193e03818b451d4570d5cd9",
# "sport_key":"basketball_nba",
# "sport_title":"NBA",
# "commence_time":"2023-05-19T00:30:00Z",
# "completed":false,
# "home_team":"Denver Nuggets",
# "away_team":"Los Angeles Lakers",
# "scores":null,"last_update":null}
# ]
class live_nba_data_route(Resource):
    def get(self):
        data = {'message': "live_nba_data_route (for game schedule)"}
        return data, 200
    def put(self):
        try:
            data =  {
                "message": "return message",
                }
            return data, 200
        except Exception as e:
            return {'message': 'Failed to put live_nba_data_route data: {}'.format(str(e))}, 500


class live_nba_odds_data(Resource):
    # def get(self):
    #     data = {'message': "live_nba_odds_data get route"}
    #     return data, 200
    def get(self):
        #example: /api/fetch-api1-data?sport=${sport}&endpoint=${endpoint}&date=${dateIsoString}`
        # maps to     
        # const oddsAPI = `https://api.the-odds-api.com/v4/sports/${sport}/${endpoint}`;
        # const apiKey = process.env.REACT_APP_ODDS_API_API_KEY;
        # //the following are defaults
        # const fullAPI = `${oddsAPI}?apiKey=${apiKey}&dateFormat=iso&date=${dateIsoString}`;
        sport = request.args.get('sport', default = "", type = str)
        endpoint = request.args.get('endpoint', default = "", type = str)
        date = request.args.get('date', default = "", type = str)
        apiKey = os.getenv("API_KEY")
        #&regions=us&markets=h2h,spreads,totals
        #example req: http://localhost:5000/api/live_nba_odds_data?sport=basketball_nba&endpoint=odds&date=2023-05-17T00:00:00Z
        odds_api_url = f"https://api.the-odds-api.com/v4/sports/{sport}/{endpoint}?apiKey={apiKey}&regions=us&markets=h2h&oddsFormat=american&dateFormat=iso&date={date}"
        #make request and store the data
        print("making request")
        try:
            response = requests.get(odds_api_url)
            response.raise_for_status()
            data = response.json()
            print("data received")
            #array of game objects in the data
            if len(data) > 0:
                print("data len greater than 0")
                for i in range(len(data)):
                    bookmakerList = data[i]["bookmakers"]
                    odds_api_game_id = data[i]["id"]
                    sport_key = sport
                    commence_time = data[i]["commence_time"]
                    #really a book data point
                    for book in bookmakerList:
                        key = book["key"]
                        odds_api_bookmaker_key = book["key"]
                        odds_api_bookmaker_title = book["title"]
                        last_update = book["last_update"]
                        #now make the query and store it if doesn't exist
                        bookMakerDataQuery = db.session.query(Bookmaker).filter(
                            Bookmaker.odds_api_game_id == odds_api_game_id,
                            Bookmaker.last_update == last_update,
                            Bookmaker.odds_api_bookmaker_key == odds_api_bookmaker_key,
                            ).all()
                        if bookMakerDataQuery is None or len(bookMakerDataQuery) == 0:
                            bookMakerObj = {
                                'odds_api_game_id': odds_api_game_id,
                                'sport_key': sport_key,
                                'odds_api_bookmaker_key': odds_api_bookmaker_key,
                                'odds_api_bookmaker_title': odds_api_bookmaker_title,
                                'commence_time': commence_time,
                                'last_update': last_update
                            }
                            #insert into db
                            _bookmaker = Bookmaker(**bookMakerObj)
                            print(_bookmaker)
                            db.session.add(_bookmaker)
                    db.session.commit()
                    return {"message": "successfully stored data in db"}, 200
            else:
                return {"message": "no games to store on the specified date"}, 200
        except Exception as e:
            return {'message': 'Failed to put live_nba_odds_data data: {}'.format(str(e))}, 500


class index_class(Resource):
    def get(self):
        return {"api-for-orca-to-db" : "index_page"}
#add resources
api.add_resource(index_class, '/api')
api.add_resource(live_nba_data_route, '/api/live-nba-data')
api.add_resource(live_nba_odds_data, '/api/live_nba_odds_data')