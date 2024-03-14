# pylint: disable=too-few-public-methods, redefined-builtin

""" Todo model Module
This module is responsible for all todos data like getting todos list from exterrnal server.
"""

import os
import requests

from src.exceptions import TodoException

class Todo():
    """Todo model
    """

    api_url = os.getenv("TODOS_PROVIDER", "https://jsonplaceholder.typicode.com/todos")

    def __init__(self, id, title):
        self.id = id
        self.title = title

    @staticmethod
    def get_todos():
        """
        :return: list of todos objects, should,
        handle server and serialization errors.
        """
        try:
            response = requests.get(Todo.api_url, timeout=3)
        except Exception:
            raise TodoException("Unable to connect to todos provider") from Exception
        if not response or response.status_code != 200:
            raise TodoException("Unable to connect to todos provider")
        response_json = response.json()
        try:
            response_filtered_objects = response_json[:5]
        except TypeError:
            raise TodoException("Unable to deserialize todos provider message") from TypeError
        return [Todo(id=todo.get('id'), title=todo.get('title'))
            for todo in response_filtered_objects]
