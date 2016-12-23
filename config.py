import os

basedir = os.path.abspath(os.path.dirname(__file__))

USERNAME = 'stockfish'
PASSWORD = '109in@now'

DATABASE_NAME = "stockfish"
SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@localhost:5432/{2}'.format(USERNAME, PASSWORD, DATABASE_NAME)
# SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

HOST = '0.0.0.0'
PORT = 5000
SECRET_KEY = '\xab\xdeL\xef\xecp\xbdQ>V\xab\x8a\xc5\x1e\x82\xc5\xc8qk\x04BG\xab1'
