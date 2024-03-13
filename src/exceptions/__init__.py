# pylint: disable=missing-module-docstring

def default_error_structure(message = ""):
    """
    Return: default error messa structure
    """
    return {  "error": {
            "reason": message,
        }
    }
