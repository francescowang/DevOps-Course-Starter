from flask import Flask, request, render_template, redirect, url_for
from todo_app.data.trello_items import TrelloItems
from todo_app.flask_config import Config
from todo_app.view_model import TaskViewModel


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    trello_items = TrelloItems()

    @app.route("/", methods=["GET"])
    def index():
        all_tasks = trello_items.get_cards()
        task_view_model = TaskViewModel(all_tasks)
        return render_template("index.html", task_view_model=task_view_model)

    # Add
    @app.route("/add_task", methods=["POST"])
    def add_task():
        trello_items.add_trello_task(title=request.form.get("item_name"))
        return redirect(url_for("index"))

    # Delete
    @app.route("/delete_task/<delete_id>", methods=["POST"])
    def delete_task(delete_id):
        trello_items.delete_trello_task(delete_task=delete_id)
        return redirect(url_for("index"))

    # Not Started
    @app.route("/not_started_task/<not_started_id>", methods=["POST"])
    def not_started_task(not_started_id):
        trello_items.not_started_trello_task(not_started_task=not_started_id)
        return redirect(url_for("index"))

    # Doing
    @app.route("/doing_task/<doing_id>", methods=["POST"])
    def doing_task(doing_id):
        trello_items.doing_trello_task(doing_task=doing_id)
        return redirect(url_for("index"))

    # Completed
    @app.route("/completed_task/<completed_id>", methods=["POST"])
    def completed_task(completed_id):
        trello_items.completed_trello_task(completed_task=completed_id)
        return redirect(url_for("index"))
    return app
