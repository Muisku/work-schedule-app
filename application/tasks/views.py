from application import app, db
from flask import redirect, render_template, request, url_for
from application.tasks.models import Task
from application.tasks.forms import TaskForm

@app.route("/tasks", methods=["GET"])
def tasks_index():
	return render_template("tasks/list.html", tasks = Task.query.all())

@app.route("/tasks/new/")
def tasks_form():
	return render_template("tasks/new.html", form = TaskForm())

@app.route("/tasks/<task_id>/", methods=["POST"])
def task_set_done(task_id):

	t = Task.query.get(task_id)
	t.done = True
	db.session().commit()

	return redirect(url_for("tasks_index"))


@app.route("/tasks/", methods=["POST"])
def tasks_create():
	form = TaskForm(request.form)

	if not form.validate():
		return render_template("tasks/new.html", form = form)

	t = Task(form.name.data)
	t.done = form.done.data	
	
	db.session().add(t)
	db.session().commit()

	return redirect(url_for("tasks_index"))
