""" Todo controller Module
This module is responsible of all todos communications
"""

from flask.views import MethodView
from flask_smorest import Blueprint

from src.models.todo import Todo


blp = Blueprint("todos", __name__, description="aaa")

@blp.route("/todo")
class TodoController(MethodView):
    """
    Todo controller
    """
    def get(self):
        """
        GET: /todo
        :return: list of todos id and title
        """
        todos = Todo.get_todos()
        return [todo.__dict__ for todo in todos]
