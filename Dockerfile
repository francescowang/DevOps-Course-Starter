FROM python:3.10.2-slim-buster as base
RUN apt-get update && apt-get install curl -y
RUN curl -sSL https://install.python-poetry.org | python3 -
COPY poetry.lock poetry.toml pyproject.toml /opt/
WORKDIR /opt
ENV PATH=$PATH:/root/.local/bin
RUN poetry config virtualenvs.create false --local && poetry install
COPY todo_app /opt/todo_app

FROM base as development
EXPOSE 5000
ENTRYPOINT poetry run flask run --host 0.0.0.0

FROM base as test
ENTRYPOINT [ "poetry", "run", "pytest" ]
COPY .env.test /opt/

FROM base as production
EXPOSE 5000
ENV PORT=80
CMD poetry run gunicorn -b 0.0.0.0:$PORT "todo_app.app:create_app()"