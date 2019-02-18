
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Nimimerkki:")
    username = StringField("Käyttäjätunnus:")
    letter = StringField("Rappu:")
    password = PasswordField("Salasana:")
    confirm = PasswordField("Vahvista Salasana:")

    class Meta:
        csrf = False