# pylint: disable=missing-module-docstring
# pylint: disable=no-value-for-parameter
# pylint: disable=no-member
# pylint: disable=broad-exception-caught

import pytest
from app import create_app
from src.controllers.user_controller import UserController

@pytest.mark.usefixtures('clean_data')
def test_user_controller_post():
    """User controller post() should create user"""
    with create_app().test_request_context(json={"user": "user_test", "password": "qwerty"}):
        user_controller = UserController()
        user = user_controller.post()
        expected_response = [b'{"id":1,"user":"user_test"}\n']
        assert user.response == expected_response


@pytest.mark.usefixtures('clean_data')
def test_user_controller_post_conflit_user():
    """User controller post() should not create existing user"""
    with create_app().test_request_context(json={"user": "user_test", "password": "qwerty"}):
        user_controller = UserController()
        user_controller.post()
        try:
            user_controller.post()
            assert False
        except Exception as error:
            error_response = [b'{"error":{"reason":"User already exists"}}\n']
            assert error.response.status_code == 409
            assert error.response.response == error_response


@pytest.mark.usefixtures('clean_data')
def test_user_controller_post_unprocessable_entity_user():
    """User controller post() should not create user without 'user'"""
    try:
        with create_app().test_request_context(json={"password": "qwerty"}):
            user_controller = UserController()
            user_controller.post()
            assert False
    except Exception as error:
        assert "422" in str(error)


@pytest.mark.usefixtures('clean_data')
def test_user_controller_post_unprocessable_entity_email():
    """User controller post() should not create user without 'password'"""
    try:
        with create_app().test_request_context(json={"user": "user_test"}):
            user_controller = UserController()
            user_controller.post()
            assert False
    except Exception as error:
        assert "422" in str(error)
