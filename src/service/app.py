import os
from flask import Flask
from flask_migrate import Migrate
from flask_appbuilder import SQLA
import logging

import models
from route import bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('MYSQL_SERVICE', '')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLA(app)

migrate = Migrate(app, db)

app.register_blueprint(bp)
app.logger.setLevel(logging.DEBUG)
