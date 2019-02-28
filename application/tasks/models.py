from application import db
from sqlalchemy.sql import text

class Task(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
	onupdate=db.func.current_timestamp())

	name = db.Column(db.String(144), nullable=False)
	done = db.Column(db.Boolean, nullable=False)

	account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=True)

	def __init__(self, name):
		self.name = name
		self.done = False

	
