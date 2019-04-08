from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Feedback(db.Model):
    __tablename__ = 'feedback'

    id = db.Column('id', db.Integer, primary_key=True)
    first_name = db.Column('first_name', db.String(20))
    last_name = db.Column('last_name', db.String(20))
    email = db.Column('email', db.String(50))
    feedback = db.Column('feedback', db.Unicode)

    def __repr__(self):
        return str(self.id) + ": " + self.first_name + " " + self.last_name
