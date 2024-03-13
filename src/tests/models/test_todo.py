# pylint: disable=missing-module-docstring

from unittest.mock import patch, Mock

from src.models.todo import Todo

@patch('requests.get')
def test_todo_model_get_todos(mock_get):
    """get_todos() should recive a todos list json and return a todo objects list"""
    mock_response = Mock()
    response_dict = [{"id": "1", "title": "title"}]
    mock_response.json.return_value = response_dict
    mock_get.return_value = mock_response
    todos = Todo.get_todos()
    expected_response = [Todo("1", "title")]

    assert len(todos) == 1
    assert todos[0].id == expected_response[0].id
    assert todos[0].title == expected_response[0].title
