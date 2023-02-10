import os, requests
from flask import Flask, request, render_template, redirect, url_for
from todo_app.flask_config import Config
from todo_app.view_model import TaskViewModel
from todo_app.data.mongodb_items import MongoDB_Items
from todo_app.users import User
from flask_login import LoginManager, login_required, login_user, current_user
from functools import wraps



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    mongo_items = MongoDB_Items()
    login_manager = LoginManager()
    
    
    @login_manager.unauthorized_handler
    def unauthenticated():
        return redirect(f"https://github.com/login/oauth/authorize?client_id={os.environ.get('CLIENT_ID')}")
    @login_manager.user_loader
    def load_user(user_id):
        return User(user_id)
    
    login_manager.init_app(app)
    @app.route("/login/callback", methods=["GET"])
    def callback():
        url = "https://github.com/login/oauth/access_token"
        code = request.args["code"]
        
        params = {
            "client_id":os.getenv("CLIENT_ID"), 
            "client_secret":os.getenv("CLIENT_SECRET"), 
            "code":code }
        header = {"Accept": "application/json"}
        response = requests.post(url, params=params, headers=header)
        oauth_token = response.json()["access_token"]
        
        api_url = "https://api.github.com/user"
        api_header = {
            "Accept":"application/vnd.github+json",
            "Authorization": f"Bearer {oauth_token}"}
        user_id = str(requests.get(api_url, headers=api_header).json()["id"])
        # print(user_id) # gets user id
        user = User(user_id)
        login_user(user)
        return redirect(url_for("index"))

    def user_authorisation(fname):
        @wraps(fname)
        def decorator(*args, **kwargs):
            if current_user.role == "admin":
                return fname(*args, **kwargs)
            else:
                return render_template("user_unathorisation.html"), 403
        return decorator
    
    @app.route("/", methods=["GET"])
    @login_required
    @user_authorisation
    def index():
        all_tasks = mongo_items.get_mongo_cards()
        task_view_model = TaskViewModel(all_tasks)
        return render_template("index.html", task_view_model=task_view_model)
    
    @app.route("/add_task", methods=["POST"])
    @login_required
    @user_authorisation
    def add_task():
        mongo_items.add_mongo_card(title=request.form.get("item_name"))
        return redirect(url_for("index"))
    
    @app.route("/delete_task/<delete_id>", methods=["POST"])
    @login_required
    @user_authorisation
    def delete_task(delete_id):
        mongo_items.delete_mongo_card(delete_id)
        return redirect(url_for("index"))
    
    @app.route("/not_started_task/<not_started_id>", methods=["POST"])
    @login_required
    @user_authorisation
    def not_started_task(not_started_id):
        mongo_items.not_started_mongo_card(id=not_started_id)
        return redirect(url_for("index"))
    
    @app.route("/doing_task/<doing_id>", methods=["POST"])
    @login_required
    @user_authorisation
    def doing_task(doing_id):
        mongo_items.doing_mongo_card(doing_id)
        return redirect(url_for("index"))
    
    @app.route("/completed_task/<completed_id>", methods=["POST"])
    @login_required
    @user_authorisation
    def completed_task(completed_id):
        mongo_items.completed_mongo_card(id=completed_id)
        return redirect(url_for("index"))
    return app
