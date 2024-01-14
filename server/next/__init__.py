import os

from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

from next import auth

load_dotenv()

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ["APP_SETTINGS"])

    db.init_app(app)

    with app.app_context():
        from next import main

        app.register_blueprint(main.main_bp, url_prefix="/app")
        app.register_blueprint(auth.auth_bp, url_prefix="/auth")
    return app
