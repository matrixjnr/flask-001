from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.config import Config, Configdb

app = Flask(__name__)

app.config.from_object(Config)
app.config.from_object(Configdb)


db = SQLAlchemy(app)
