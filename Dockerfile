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

# this test stage is needed for continuous integration
FROM base as test
ENTRYPOINT [ "poetry", "run", "pytest" ]

# this production stage is deliberately the final stage of this file, so that it's the default
# you can make changes in production in docker
# you have to rebuild the docker image
FROM base as production
EXPOSE 5000
ENV PORT=80
ENTRYPOINT poetry run gunicorn -b 0.0.0.0:$PORT "todo_app.app:create_app()"
