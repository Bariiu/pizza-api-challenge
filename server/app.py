from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from server.config import DATABASE_URI

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Migrate(app, db)

    return app

app = create_app()
