from flask import Flask, request, render_template, redirect, url_for
# from todo_app.data.trello_items import TrelloItems
from todo_app.flask_config import Config
from todo_app.view_model import TaskViewModel
from todo_app.data.mongodb_items import MongoDB_Items


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    mongo_items = MongoDB_Items()

    @app.route("/", methods=["GET"])
    def index():
        all_tasks = mongo_items.get_mongo_cards()
        task_view_model = TaskViewModel(all_tasks)
        return render_template("index.html", task_view_model=task_view_model)

    # Add
    @app.route("/add_task", methods=["POST"])
    def add_task():
        mongo_items.add_mongo_card(title=request.form.get("item_name"))
        return redirect(url_for("index"))

    # Delete
    @app.route("/delete_task/<delete_id>", methods=["POST"])
    def delete_task(delete_id):
        mongo_items.delete_mongo_card(delete_id)
        return redirect(url_for("index"))

    # Not Started
    @app.route("/not_started_task/<not_started_id>", methods=["POST"])
    def not_started_task(not_started_id):
        mongo_items.not_started_mongo_card(id=not_started_id)
        return redirect(url_for("index"))

    # Doing
    @app.route("/doing_task/<doing_id>", methods=["POST"])
    def doing_task(doing_id):
        mongo_items.doing_mongo_card(doing_id)
        return redirect(url_for("index"))

    # Completed
    @app.route("/completed_task/<completed_id>", methods=["POST"])
    def completed_task(completed_id):
        mongo_items.completed_mongo_card(id=completed_id)
        return redirect(url_for("index"))
    return app
