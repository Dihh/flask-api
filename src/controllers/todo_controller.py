""" Todo controller Module
This module is responsible of all todos communications
"""

from flask.views import MethodView
from flask_smorest import Blueprint
from src.schemas.todo_schema import TodoSchema

from src.models.todo import Todo


blp = Blueprint("todos", __name__, description="aaa")

@blp.route("/todo")
class TodoController(MethodView):
    """Todo controller
    """
    @blp.response(200, TodoSchema(many=True))
    def get(self):
        """
        return: list of todos with id and title
        """
        return Todo.get_todos()
