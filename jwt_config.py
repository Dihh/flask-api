# pylint: disable=unused-argument

""" jwt module
reset some jwt configurations.
"""

from flask import jsonify

from src.exceptions import default_error_structure

def config_jwt(jwt):
    """
    reset jwt default returns messages.
    """

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(default_error_structure("The token has expired.")),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(default_error_structure("Signature verification failed.")),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(default_error_structure("Request does not contain an access token.")),
            401,
        )

    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header, jwt_payload):
        return (
            jsonify(default_error_structure("The token is not fresh.")),
            401,
        )

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(default_error_structure("The token has been revoked.")),
            401,
        )
