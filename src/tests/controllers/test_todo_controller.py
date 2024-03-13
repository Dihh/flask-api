# pylint: disable=missing-module-docstring

from unittest.mock import patch

from src.controllers.todo_controller import TodoController
from src.models.todo import Todo as TodoModel

@patch('src.models.todo.Todo.get_todos')
def test_todo_controller_get(mock_get):
    """Todo controller get() should serialize response"""
    response_dict = [TodoModel(id="1", title="title")]
    mock_get.return_value = response_dict
    todo_controller = TodoController()
    todos = todo_controller.get()
    expected_response = [{"id": "1", "title": "title"}]
    assert todos == expected_response
