""" Models Package
This package is responsible for share all custom exceptions through the system
"""

from src.exceptions.todo_exception import *

def default_error_structure(message = ""):
    """
    Return: default error messa structure
    """
    return {  "error": {
            "reason": message,
        }
    }
