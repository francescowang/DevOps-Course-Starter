FROM python:3.10.2-slim-buster as base: This sets the base image for the Dockerfile to Python 3.10.2 on a slimmed down version of the Debian Buster operating system.

RUN apt-get update && apt-get install curl -y: This updates the package index on the container and installs the curl package.

RUN curl -sSL https://install.python-poetry.org | python3 -: This downloads and installs the Poetry package manager for Python.

COPY poetry.lock poetry.toml pyproject.toml /opt/: This copies the Poetry lock file and project configuration files to the /opt/ directory in the container.

WORKDIR /opt: This sets the working directory for the container to /opt/.

ENV PATH=$PATH:/root/.local/bin: This sets the PATH environment variable to include the Poetry executable, so that it can be used in subsequent commands.

RUN poetry config virtualenvs.create false --local && poetry install: This configures Poetry to not create a virtual environment, and then installs the dependencies for the Flask application.

COPY todo_app /opt/todo_app: This copies the source code for the Flask application to the /opt/todo_app directory in the container.

FROM base as development: This creates a new image based on the base image.

EXPOSE 5000: This exposes port 5000 on the container.

ENTRYPOINT poetry run flask run --host 0.0.0.0: This sets the entrypoint command for the container to run the Flask application using the flask run command.

FROM base as test: This creates a new image based on the base image.

ENTRYPOINT [ "poetry", "run", "pytest" ]: This sets the entrypoint command for the container to run the tests using the pytest command.

COPY .env.test /opt/: This copies the test environment variables file to the /opt/ directory in the container.

FROM base as production: This creates a new image based on the base image.

EXPOSE 5000: This exposes port 5000 on the container.

ENV PORT=80: This sets the PORT environment variable to 80.

CMD poetry run gunicorn -b 0.0.0.0:$PORT "todo_app.app:create_app()": This sets the default command for the container to run the Gunicorn web server with the Flask application, listening on all interfaces on the specified port.

