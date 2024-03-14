# pylint: disable=missing-module-docstring
# pylint: disable=no-member
# pylint: disable=broad-exception-caught

from unittest.mock import patch

from flask_jwt_extended import create_access_token

from app import create_app
from src.exceptions import TodoException
from src.controllers.todo_controller import TodoController
from src.models.todo import Todo as TodoModel

@patch('src.models.todo.Todo.get_todos')
def test_todo_controller_get(mock_get_todos):
    """Todo controller get() should serialize response"""
    response_dict = [TodoModel(id="1", title="title")]
    mock_get_todos.return_value = response_dict
    todo_controller = TodoController()
    with create_app().app_context():
        access_token = create_access_token(identity='')
    with create_app().test_request_context(headers={"Authorization": f"Bearer {access_token}"}):
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
        access_token = create_access_token(identity='')
    with create_app().test_request_context(headers={"Authorization": f"Bearer {access_token}"}):
        try:
            todo_controller.get()
            assert False
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
        access_token = create_access_token(identity='')
    with create_app().test_request_context(headers={"Authorization": f"Bearer {access_token}"}):
        try:
            todo_controller.get()
            assert False
        except Exception as error:
            expected_response = [b'{"error":{"reason":"todo erro message"}}\n']
            assert error.response.response == expected_response


@patch('src.models.todo.Todo.get_todos')
def test_todo_controller_get_should_not_execute_without_authenticated_user(mock_get_todos):
    """
    Todo controller get() should return serialized 
    'todo erro message' json when Todo errors occur
    """
    mock_get_todos.side_effect=TodoException('todo erro message')
    todo_controller = TodoController()
    with create_app().test_request_context(headers={}):
        try:
            todo_controller.get()
            assert False
        except Exception as error:
            assert "Missing Authorization Header" in str(error)


@patch('src.models.todo.Todo.get_todos')
def test_todo_controller_get_should_not_execute_with_invalid_token(mock_get_todos):
    """
    Todo controller get() should return serialized 
    'todo erro message' json when Todo errors occur
    """
    mock_get_todos.side_effect=TodoException('todo erro message')
    todo_controller = TodoController()
    with create_app().app_context():
        access_token = create_access_token(identity='')
    with create_app().test_request_context(headers={
            "Authorization": f"Bearer {access_token}invalidtoken"
        }):
        try:
            todo_controller.get()
            assert False
        except Exception as error:
            assert "Signature verification failed" in str(error)
