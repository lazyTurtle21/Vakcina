from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)
db = SQLAlchemy(app)

class ClientLog(UserMixin, db.Model):
    __tablename__ = 'client_log'
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    first = db.Column(db.Boolean)


class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, db.ForeignKey('client_log.id'), primary_key=True, nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    sex = db.Column(db.Integer, nullable=False)
    date_of_birth = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)


    def __repr__(self):
        return str({'id': self.id,
                    'first_name': self.first_name,
                    'last_name': self.last_name,
                    'sex': self.sex,
                    'date_of_birth': self.date_of_birth,
                    'location': self.location})


class Vaccines(db.Model):
    __tablename__ = 'vaccines'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return str({'id': self.id,
                    'name': self.name})


class AgeVaccination(db.Model):
    __tablename__ = 'age_vaccination'
    vacc_id = db.Column(db.Integer, db.ForeignKey('vaccines.id'), primary_key=True)
    age = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return str({'vacc_id': self.vacc_id,
                    'age': self.age})


class VaccControl(db.Model):
    __tablename__ = 'vacc_control'
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), primary_key=True)
    vacc_id = db.Column(db.Integer, db.ForeignKey('vaccines.id'), primary_key=True)
    is_done = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return str({'client_id': self.client_id,
                    'vacc_id': self.vacc_id,
                    'is_done': self.is_done})
