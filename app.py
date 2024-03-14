# pylint: disable=missing-module-docstring

import os
from flask import Flask
from flask_smorest import Api
from src.controllers.user_controller import blp as UserController
from db import db
import src.models # pylint: disable=unused-import

from src.controllers.todo_controller import blp as TodoController

def create_app():
    """
    initial function with all the information to create the application and database communication
    """
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = False
    app.config["API_TITLE"] = "Flask todos API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///data.db")
    db.init_app(app)

    with app.app_context():
        db.create_all()

    api = Api(app)

    api.register_blueprint(TodoController)
    api.register_blueprint(UserController)
    return app
