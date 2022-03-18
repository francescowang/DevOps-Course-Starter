from flask import Flask, request, render_template, redirect, url_for
from todo_app.data.trello_items import (
    get_cards,
    add_trello_task,
    delete_trello_task,
    not_started_trello_task,
    doing_trello_task,
    completed_trello_task,
)
from todo_app.flask_config import Config
from todo_app.view_model import TaskViewModel


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route("/", methods=["GET"])
    def index():
        all_tasks = get_cards()
        task_view_model = TaskViewModel(all_tasks)
        return render_template("index.html", task_view_model=task_view_model)

    # Add
    @app.route("/add_task", methods=["POST"])
    def add_task():
        add_trello_task(title=request.form.get("item_name"))
        return redirect(url_for("index"))

    # Delete
    @app.route("/delete_task/<delete_id>", methods=["POST"])
    def delete_task(delete_id):
        delete_trello_task(delete_task=delete_id)
        return redirect(url_for("index"))

    # Not Started
    @app.route("/not_started_task/<not_started_id>", methods=["POST"])
    def not_started_task(not_started_id):
        not_started_trello_task(not_started_task=not_started_id)
        return redirect(url_for("index"))

    # Doing
    @app.route("/doing_task/<doing_id>", methods=["POST"])
    def doing_task(doing_id):
        doing_trello_task(doing_task=doing_id)
        return redirect(url_for("index"))

    # Completed
    @app.route("/completed_task/<completed_id>", methods=["POST"])
    def completed_task(completed_id):
        completed_trello_task(completed_task=completed_id)
        return redirect(url_for("index"))
    return app


if __name__ == "__main__":
    create_app.run()
