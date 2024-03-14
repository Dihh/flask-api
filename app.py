# pylint: disable=missing-module-docstring

import os
import logging
from flask import Flask
from flask_migrate import Migrate
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from jwt_config import config_jwt

from db import db
from src.controllers.user_controller import blp as UserController
from src.controllers.todo_controller import blp as TodoController
import src.models # pylint: disable=unused-import

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def set_api_config(app: Flask) -> None:
    """
    set app configurations
    """
    app.config["PROPAGATE_EXCEPTIONS"] = False
    app.config["API_TITLE"] = "Flask todos API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

def set_db(app: Flask) -> None:
    """
    set database configurations
    """
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///data.db")
    db.init_app(app)
    Migrate(app, db)

def set_api(app: Flask) -> Api:
    """
    set api configurations
    """
    api = Api(app)
    api.spec.components.security_scheme("bearerAuth", {
        "type": "http", "scheme": "bearer", "bearerFormat": "JWT"
    })
    return api

def set_jwt(app: Flask) -> None:
    """
    set jwt configurations
    """
    app.config["JWT_SECRET_KEY"] = os.getenv(
        "JWT_SECRET_KEY", "cc878440-91e0-4a07-b893-ef83b97a3256"
    )
    jwt = JWTManager(app)
    config_jwt(jwt)

def register_blueprint(api: Api) -> None:
    """
    register blueprints on api
    """
    api.register_blueprint(TodoController)
    api.register_blueprint(UserController)


def create_app() -> Flask:
    """
    initial function with all the information to create the application and database communication
    """
    app = Flask(__name__)

    set_api_config(app)
    set_db(app)
    api = set_api(app)
    set_jwt(app)
    register_blueprint(api)

    return app
