from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)

    loans = db.relationship('Loan', backref='user', lazy=True)


class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    interest = db.Column(db.Numeric(10, 2), nullable=False)
    start_date = db.Column(db.String(20), nullable=False)  
    loan_status = db.Column(db.String(20), default='Active', nullable=False) 

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

