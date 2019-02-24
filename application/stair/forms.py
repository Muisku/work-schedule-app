
from flask_wtf import FlaskForm
from wtforms import StringField

class StairForm(FlaskForm):
    stair_letter = StringField("Rappu:")

    class Meta:
        csrf = False