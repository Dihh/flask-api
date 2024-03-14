# pylint: disable=missing-module-docstring
# pylint: disable=no-member
# pylint: disable=broad-exception-caught

from unittest.mock import patch

from app import create_app
from src.exceptions.todo_exception import TodoException
from src.controllers.todo_controller import TodoController
from src.models.todo import Todo as TodoModel

@patch('src.models.todo.Todo.get_todos')
def test_todo_controller_get(mock_get_todos):
    """Todo controller get() should serialize response"""
    response_dict = [TodoModel(id="1", title="title")]
    mock_get_todos.return_value = response_dict
    todo_controller = TodoController()
    with create_app().app_context():
        todos = todo_controller.get()
        expected_response = [b'[{"id":1,"title":"title"}]\n']
        assert todos.response == expected_response


@patch('src.models.todo.Todo.get_todos')
def test_todo_controller_get_should_send_error_formated(mock_get_todos):
    """
    Todo controller get() should return serialized 
    'Internal Server Erro' json when default errors occur
    """
    mock_get_todos.side_effect=Exception()
    todo_controller = TodoController()
    with create_app().app_context():
        try:
            todo_controller.get()
        except Exception as error:
            expected_response = [b'{"error":{"reason":"Internal Server Error"}}\n']
            assert error.response.response == expected_response


@patch('src.models.todo.Todo.get_todos')
def test_todo_controller_get_should_send_todo_error_formated(mock_get_todos):
    """
    Todo controller get() should return serialized 
    'todo erro message' json when Todo errors occur
    """
    mock_get_todos.side_effect=TodoException('todo erro message')
    todo_controller = TodoController()
    with create_app().app_context():
        try:
            todo_controller.get()
        except Exception as error:
            expected_response = [b'{"error":{"reason":"todo erro message"}}\n']
            assert error.response.response == expected_response
