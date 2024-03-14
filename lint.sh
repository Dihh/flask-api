#! /bin/bash

docker-compose exec backend bash -c "pylint *.py"