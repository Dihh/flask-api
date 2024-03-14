#! /bin/bash

export DATABASE_URL=sqlite:///test.db
flask db upgrade
python -m pytest -sv --cov-report html src/tests --cov=./