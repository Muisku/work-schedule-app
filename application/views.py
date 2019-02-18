from flask import render_template
from application import app
from application.auth.models import User
from application.tasks.models import Task

@app.route("/")
def index():
	return render_template("index.html", needs_tasks=User.find_users_with_no_tasks())

@app.route("/users")
def index2():
	return render_template("index2.html", all_users=User.find_users())

@app.route("/test")
def index3():
	return render_template("index3.html", users_tasks=User.find_users_tasks())