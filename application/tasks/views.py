from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.tasks.models import Task
from application.tasks.forms import TaskForm

from sqlalchemy.sql import text








@app.route("/tasks/new/")
@login_required
def tasks_form():
	return render_template("tasks/new.html", form = TaskForm())


@app.route("/tasks/", methods=["POST"])
@login_required
def tasks_create():
	form = TaskForm(request.form)

	if not form.validate():
		return render_template("tasks/new.html", form = form)

	t = Task(form.name.data)
	t.done = form.done.data	
	t.account_id = current_user.id
	
	db.session().add(t)
	db.session().commit()

	return redirect(url_for("tasks_index"))



@app.route("/tasks", methods=["GET"])
def tasks_index():
	return render_template("tasks/list.html", tasks = Task.query.all())
	

@app.route("/tasks/<task_id>/", methods=["POST"])

def task_set_done(task_id):

	t = Task.query.get(task_id)
	t.done = True
	db.session().commit()


	return redirect(url_for("tasks_index"))

@app.route("/tasks/<id_a>/rm", methods=["POST"])
def task_remove(id_a):

	c = Task.query.get(id_a)
	db.session().delete(c)
	db.session().commit()

	return redirect(url_for("tasks_index"))

@app.route("/tasks/<id_g>/edit", methods = ["GET"])
def edit_task(id_g):
	form = TaskForm(request.form)
	form.name.data = Task.query.get(id_g).name
	return render_template("tasks/edit.html", task = Task.query.get(id_g), form = form)

@app.route("/tasks/<id_g>/update", methods = ["POST"])
def update_task(id_g):
	form = TaskForm(request.form)
	task = Task.query.get(id_g)
	task.name = form.name.data
	db.session().commit()
	
	return redirect(url_for('tasks_index'))

