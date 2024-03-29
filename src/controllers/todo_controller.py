""" Todo controller Module
This module is responsible of all todos communications
"""

from flask import make_response
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort
from src.exceptions import TodoException
from src.exceptions import default_error_structure
from src.schemas import SystemErrorSchema, TodoSchema

from src.models.todo import Todo


blp = Blueprint("todos", __name__)

@blp.route("/todo")
class TodoController(MethodView):
    """Todo controller
    """
    @jwt_required()
    @blp.doc(security=[{"bearerAuth": []}])
    @blp.response(500, SystemErrorSchema)
    @blp.response(200, TodoSchema(many=True))
    def get(self):
        """
        return: list of todos with id and title
        """
        try:
            todos = Todo.get_todos()
            return todos
        except TodoException as error:
            error_message = default_error_structure(str(error))
            response = make_response(error_message, 500)
            abort(response)
        except Exception:
            error_message = default_error_structure("Internal Server Error")
            response = make_response(error_message, 500)
            abort(response)
