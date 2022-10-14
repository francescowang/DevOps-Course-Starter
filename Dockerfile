#  https://github.com/docker-library/python/blob/master/3.10/slim-buster/Dockerfile
FROM python:3.10.2-slim-buster as base
# apt-get update -> updates the package lists for upgrades for packages that need upgrading, 
# as well as new packages that have just come to the repositories.
# 
RUN apt-get update && apt-get install curl -y
RUN curl -sSL https://install.python-poetry.org | python3 -
COPY poetry.lock poetry.toml pyproject.toml /opt/
WORKDIR /opt
# /Users/fwang29/.poetry/bin or ~fwang29/.poetry/bin
ENV PATH=$PATH:/root/.local/bin
RUN poetry config virtualenvs.create false --local && poetry install
COPY todo_app /opt/todo_app

# you can make changes in localhost in docker
# you don't need to rebuild a docker image
FROM base as development
EXPOSE 5000
ENTRYPOINT poetry run flask run --host 0.0.0.0

# this test stage is needed for continuous integration
FROM base as test
ENTRYPOINT [ "poetry", "run", "pytest" ]
COPY .env.test /opt/

# this production stage is deliberately the final stage of this file, so that it's the default
# you can make changes in production in docker
# you have to rebuild the docker image
FROM base as prod
EXPOSE 5000
ENV PORT=80
CMD poetry run gunicorn -b 0.0.0.0:$PORT "todo_app.app:create_app()"
