# pylint: disable=missing-module-docstring
# pylint: disable=dangerous-default-value

from unittest.mock import patch, Mock

from src.exceptions.todo_exception import TodoException

from src.models.todo import Todo

def set_mock_response(response_dict = [{"id": "1", "title": "title"}], status_code=200):
    """
    Return mock function for requests.get mocked tests
    """
    mock_response = Mock()
    mock_response.json.return_value = response_dict
    mock_response.status_code = status_code
    return mock_response


@patch('requests.get')
def test_todo_model_get_todos(mock_get):
    """get_todos() should recive a todos list json and return a todo objects list"""
    mock_get.return_value = set_mock_response()
    todos = Todo.get_todos()
    expected_response = [Todo("1", "title")]

    assert len(todos) == 1
    assert todos[0].id == expected_response[0].id
    assert todos[0].title == expected_response[0].title
    mock_get.assert_called_once()


@patch('requests.get')
def test_todo_model_get_todos_server_error(mock_get):
    """get_todos() should handle error when server communication fail"""
    mock_get.return_value = set_mock_response(status_code=404)
    try:
        Todo.get_todos()
    except TodoException as error:
        assert str(error) == "Unable to connect to todos provider"


@patch('requests.get')
def test_todo_model_get_todos_json_serization_error(mock_get):
    """get_todos() should handle error when serialization fail"""
    mock_get.return_value = set_mock_response(False)
    try:
        Todo.get_todos()
    except TodoException as error:
        assert str(error) == "Unable to deserialize todos provider message"
