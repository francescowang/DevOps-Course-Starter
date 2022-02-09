from flask import Flask, request, render_template, redirect, url_for
from todo_app.data.session_items import get_items, get_item, add_item, delete_item, save_item
from todo_app.flask_config import Config


app = Flask(__name__)
app.secret_key="WHY!"
app.config.from_object(Config)


@app.route('/', methods=['GET'])
def index():
    items = get_items()
    items.sort(key = lambda task: task['status'], reverse=True) # status refers to a key in session_items on line 4
    return render_template('index.html', items_jinja=items) # items_jinja refers to index.html on line 15


@app.route('/add_task', methods=['POST'])
def add_task():
    add_item(title=request.form.get('item_name'))
    return redirect(url_for('index'))


@app.route('/delete/<item_id>', methods=['POST'])
def delete_task(item_id):
    item = get_item(item_id)
    delete_item(task=item)
    return redirect(url_for('index'))    


@app.route('/completed/<item_id>', methods=['POST'])
def mark_as_complete(item_id):
    item = get_item(item_id)
    item["status"] = "Completed"
    save_item(task=item) # key -> that's the parameter of the function save_item(), line 62
    return redirect(url_for('index'))


@app.route('/not_started/<item_id>', methods=['POST'])
def mark_as_to_do(item_id):
    item = get_item(item_id)
    item["status"] = "Not Started"
    save_item(task=item)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()