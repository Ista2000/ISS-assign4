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


class Quiz(db.Model):
    __tablename__ = 'quiz_submissions'

    id = db.Column('id', db.Integer, primary_key=True)
    sub_q1 = db.Column('q1', db.String(10))
    sub_q2 = db.Column('q2', db.String(10))
    sub_q3 = db.Column('q3', db.String(10))
    sub_q4 = db.Column('q4', db.String(10))
    sub_q5 = db.Column('q5', db.String(120))

    def __repr__(self):
        return str(self.id)
