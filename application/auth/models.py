from application import db
from sqlalchemy.sql import text

class User(db.Model):

    __tablename__ = "account"
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    letter = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    tasks = db.relationship("Task", backref='account', lazy=True)
    stair = db.relationship("Stair", backref='account', lazy=True)

    

    def __init__(self, name, username, letter, password):
        self.name = name
        self.username = username
        self.letter = letter
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod
    def find_users_with_no_tasks():
        stmt = text("SELECT Account.id, Account.name FROM Account"
                    " LEFT JOIN Task ON Task.account_id = Account.id"
                    " WHERE (Task.done IS null OR Task.done = 1)"
                    " GROUP BY Account.id"
                    " HAVING COUNT(Task.id) = 0")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response

    @staticmethod
    def find_users_tasks():
        stmt = text("SELECT account.name, task.name, task.done FROM Account, Task"
                    " WHERE Account.id = Task.account_id")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0], "task_name":row[1], "done":row[2]})

        return response

    @staticmethod
    def find_users():
        stmt = text("SELECT Account.id, Account.name, Account.letter FROM Account"
                    " LEFT JOIN Task ON Task.account_id = Account.id")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "letter":row[2]})

        return response       










    """ @staticmethod
	def find_users_tasks():
		stmt = text("SELECT account.name, task.name, task.done FROM Account, Task"
					" WHERE Account.id = Task.account_id")
		res = db.engine.execute(stmt)

		response = []
		for row in res:
			response.append({"name":row[0], "task_name":row[1], "done":row[2]})

		return response
         """
    
		
     


  