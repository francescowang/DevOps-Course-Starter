from flask import Flask, request, render_template, redirect, url_for
from todo_app.data.trello_items import *
from todo_app.flask_config import Config


app = Flask(__name__)
app.config.from_object(Config())


@app.route("/", methods=["GET"])
def index():
    not_started_tasks = get_cards("NOT STARTED")
    doing_tasks = get_cards("DOING")
    completed_tasks = get_cards("COMPLETED")
    return render_template(
        "index.html",
        not_started_tasks=not_started_tasks,
        doing_tasks=doing_tasks,
        completed_tasks=completed_tasks,
    )


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


if __name__ == "__main__":
    app.run()