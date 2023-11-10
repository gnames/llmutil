from flask import Flask

from app.config import Config
app = Flask(__name__)
app.version = 'v0.0.1'
app.config.from_object(Config)

from app import routes

