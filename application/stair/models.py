from application import db

class Stair(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def get_id(self):
        return self.id