from flask import Flask
from flask.ext.sqlalchemy import SQLALchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLALchemy(app)

from app import views, models
