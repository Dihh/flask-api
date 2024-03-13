# pylint: disable=too-few-public-methods, redefined-builtin

""" Todo model Module
This module is responsible for all todos data like getting todos list from exterrnal serverr
"""

import requests

class Todo():
    """Todo model
    """

    api_url = 'https://jsonplaceholder.typicode.com/todos'

    def __init__(self, id, title):
        self.id = id
        self.title = title

    @staticmethod
    def get_todos():
        """
        :return: list of todos objects, should,
        handle server and serialization errors.
        """
        response = requests.get(Todo.api_url, timeout=3)
        response_json = response.json()[:5]
        return [Todo(id=todo.get('id'), title=todo.get('title'))
            for todo in response_json]
