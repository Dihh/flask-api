# pylint: disable=broad-exception-caught

""" User controller Module
This module is responsible of all users communications
"""

import logging
from flask import make_response
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token

from db import db
from src.schemas.auth_schema import SystemAuthSchema
from src.schemas.error_schema import SystemErrorSchema
from src.exceptions import default_error_structure
from src.schemas.schemas import UserSchema
from src.models.users import UserModel

blp = Blueprint("users", __name__)

@blp.route("/login")
class UserAuthController(MethodView):
    """User controller
    """
    @blp.arguments(UserSchema)
    @blp.response(422, SystemErrorSchema)
    @blp.response(200, SystemAuthSchema)
    def post(self, user_data):
        """
        return: list of todos with id and title
        """
        user = UserModel.query.filter(UserModel.user == user_data["user"]).first()

        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity=user.id)
            logging.info("%s - POST /login 200", user.user)
            return {"access_token": access_token}

        error_message = default_error_structure("Invalid credentials.")
        response = make_response(error_message, 401)
        logging.info("%s - POST /login 401", user_data["user"])
        abort(response)

@blp.route("/register")
class UserController(MethodView):
    """User controller
    """
    @blp.arguments(UserSchema)
    @blp.response(409, SystemErrorSchema)
    @blp.response(422, SystemErrorSchema)
    @blp.response(201, UserSchema)
    def post(self, user_data):
        """
        return: list of todos with id and title
        """
        if UserModel.query.filter(UserModel.user == user_data["user"]).first():
            error_message = default_error_structure("User already exists")
            response = make_response(error_message, 409)
            logging.info("%s - POST /register 409", user_data["user"])
            abort(response)

        user = UserModel(user=user_data["user"], password=pbkdf2_sha256.hash(user_data["password"]))
        try:
            db.session.add(user)
            db.session.commit()
        except SQLAlchemyError:
            error_message = default_error_structure("Unable to save this user")
            response = make_response(error_message, 422)
            logging.info("%s - POST /register 422", user_data["user"])
            abort(response)
        user_info = {"user": user_data["user"], "id": user.id}
        logging.info("%s - POST /register 201", user_info)
        return user, 201
