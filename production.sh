#! /bin/bash

flask db upgrade &&
waitress-serve --call --port=$PORT 'app:create_app'