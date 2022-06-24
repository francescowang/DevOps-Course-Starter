FROM python:3.10.2-slim-buster as base
RUN apt-get update && apt-get install curl -y
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
COPY poetry.lock poetry.toml pyproject.toml /opt/
WORKDIR /opt
ENV PATH=$PATH:/root/.poetry/bin
RUN poetry install
COPY . /opt/

# you can make changes in localhost in docker
# you don't need to rebuild a docker image
FROM base as development
EXPOSE 5000
ENTRYPOINT poetry run flask run --host 0.0.0.0

# you can make changes in production in docker
# you have to rebuild the docker image
FROM base as production
EXPOSE 5000
ENTRYPOINT poetry run gunicorn -b 0.0.0.0 "todo_app.app:create_app()"
