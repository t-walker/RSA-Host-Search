# Imports for the Application
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
# End Imports


# Application Configuration
app = Flask(__name__)
app.config.from_object('config')


db = SQLAlchemy(app)
# End Configuration

from app import views, models
