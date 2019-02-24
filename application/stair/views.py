from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application.stair.models import Stair
from application.stair.forms import StairForm

from sqlalchemy.sql import text


@app.route("/stairs/new/")
def stairs_form():
	return render_template("stairs/new.html", form = StairForm())



@app.route("/stairs/", methods=["POST"])
def stairs_create():
	form = StairForm(request.form)

	if not form.validate():
		return render_template("tasks/new.html", form = form)

	t = Stair(form.stair_letter.data)
	t.account_id = current_user.id
	
	db.session().add(t)
	db.session().commit()

	return redirect(url_for("tasks_index"))
    
