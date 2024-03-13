# pylint: disable=missing-module-docstring

class TodoException(Exception):
    """
    Class for todos errors
    """
    def __init__(self, message):
        super().__init__(message)
