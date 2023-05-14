import os
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config as CFG
from datetime import timedelta
from werkzeug.middleware.proxy_fix import ProxyFix
#note if insalling manually:
# pip install mysqlclient (mix os/ python 3)
#apk install mariadb-dev
# otherwise:
# python3 -m pip install package
db = SQLAlchemy()
def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config['SQLALCHEMY_DATABASE_URI'] = CFG.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = "sxasd342r2q345gasdg"
    db.init_app(app)

    with app.app_context():
        from . import models
        db.create_all()
        from . import api_routes
        app.register_blueprint(api_routes.api_main)
        # app.wsgi_app = ProxyFix(
        #     app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
        # )
        jwt = JWTManager(app)
        CORS(app, resources={r'/api/*': {"origins": "*"}}, methods=['GET', 'PUT', 'POST'])
        return app
