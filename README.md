# Cleaning company

This system was developed to be used as a todos API, so... lets see how it works:

By default SQLite database will be used and connected by a Python (flask) backend. This database can be easily changed using DATABASE_URL environment variables.

The backend uses pylint to maintain code quality, pytest for testing, SQLAlchemy for ORM and  Alembic for migrations.

There are three different way to run this project: **Docker Compose**, **Docker** and **local**.

## Tools versions
- Docker version 25.0.2
- python version 3.12
- flask version 3.0.2

## Docker Compose

You can easily run this project with `docker compose`, just clone this project, go to the project folder and run:

```sh
$ docker compose up
```
 
The  `Dockerfile` and `docker-compose.yml` has the necessary configuration to install dependencies and define environment variables to start the system.

The `docker-compose.yml` has 3 important environment variables:

```yaml
environment:
    - DATABASE_URL=sqlite:///data.db
    - JWT_SECRET_KEY=cc878440-91e0-4a07-b893-ef83b97a3256
    - TODOS_PROVIDER=https://jsonplaceholder.typicode.com/todos
```

* DATABASE_URL: specifies how the backend will communicate with the database.
* JWT_SECRET_KEY: specifies the secret key to validate the tokens.
* TODOS_PROVIDER: specifies the todos provider URL.

## Docker

```sh
$ docker build . --tag 'image_name'
$ docker run -it -e PORT=5000 -p 5000:5000 image_name
```

You can change `PORT` if this is necessary.

## Local

To run this project in a local environment you will need python3.12 installed, and run start.sh

## API Documentations

This system uses swagger as an API documentation and you can learn how to communicate with this API in the route `/swagger-ui`

![swagger picture](https://github.com/Dihh/flask-api/blob/main/documentation/swagger.png)

In swagger after login you can store the user token in the `Authorize` button without 'bearer' to fetch authorized routes.

A postman collection can also be used as API documentation and you can import the `flaskAPI.postman_collection.json` file into your postman.

# System structure 

The folder structure follows the MVC principles using `controllers` for managing the incoming data and models for database/server communication.

```
src
└── controllers
│	│
│	└──todo_controller.py
│	└──user_controller.py
│
│
└── models
│	│
│	└──todo.py
│	└──user.py
│
│
└── exceptions  #To store custom system exceptions
│	│
│	└──todo_exceptions.py
│
│
└── schemas  #To store API schemas
│	│
│	└──schemas.py
│
│
└── tests
```

## Tests

#### Unit tests
Model tests can be used as unit tests of this application, they mock external communication and ensure the correct application behavior in diferent contexts

#### e2e tests
Controller's tests can be used as e2e tests of this application, as they will store and read some data from a test database. The database will be cleaned before each test thanks to a fixture.

You can run the tests using: 
* `$ bash test.sh` - In a unix system with docker compose instaled (with container running).
* `$ docker exec CONTAINER_ID bash -c "bash run_tests.sh"` - In any system with docker (with container running) change 
CONTAINER_ID for a valid container id.
* `$ bash run_tests.sh` - In any unix system with python.

You can generate the test coverage report by running `run_tests.sh`, but you will need to map it outside the container in docker contexts, the docker compose solution already does this.

The test coverage is almost 95% as you can see below:

![test coverage picture](https://github.com/Dihh/flask-api/blob/main/documentation/test-coverage.png)

## Lint

The lint configuration ensures code quality.

* `$ bash lint.sh` - In a unix system with docker compose instaled (with container running).
* `$ docker exec CONTAINER_ID bash -c "pylint *.py"` - In any system with docker (with container running) change 
CONTAINER_ID for a valid container id.
* `$ pylint *.py` - In any system with python and pylint instaled.

## Production x Development environment

The dockerfile will start with `waitress-serve` if the default --entrypoint is not replaced.

The docker-compose will replace the default --entrypoint with `flask run` with debugging enabled.

Waitress-serve is recommended for production.

## Dependencies

Pip with requirements.txt was chosen to manage dependencies. `Dockerfile` and `docker-compose.yml` will automatically install the dependencies when start the system.

* requests - Used for http communication necessary to get todos.
* pytest - Used to run tests.
* flask-smorest - Used for serializations, deserializations and validations.
* mock - Used to mock same function and external communications.
* pylint - Used to run the system lint configuration.
* marshmallow - Used with flask-smorest for serializations and data convecions.
* pytest-cov - Test coverage report.
* Flask-SQLAlchemy - ORM.
* passlib - Encripty password.
* Flask-JWT - Manager tokens.
* Flask-Migrate - Migrations.
* waitress - Production server.

## logging

The system logs all requests with `logging` and can be followed in terminal or redirected to files or servers if necessary.

All requests are logged with date, time, response data and HTTP status code.

## Pipeline

The system has a pipeline that will ensure that the tests are not failing, the lint is as expected and if the previous two steps are executed successfully, a deployment will be executed.

![pipeline picture](https://github.com/Dihh/flask-api/blob/main/documentation/pipeline.png)

This pipeline will run on Github Actions.