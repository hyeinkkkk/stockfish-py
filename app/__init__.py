from flask import Flask, redirect, url_for
# from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.do')
app.config.from_object('config')

db = SQLAlchemy(app)

from app import apis
