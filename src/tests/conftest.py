""" conftest module
Used to store tests fixtures.
"""

import pytest
from app import create_app
from db import db


@pytest.fixture()
def clean_data():
    """
    Fixture to clean database before some tests.
    """
    with create_app().app_context():
        meta = db.metadata
        for table in reversed(meta.sorted_tables):
            db.session.execute(table.delete())
        db.session.commit()
    yield
