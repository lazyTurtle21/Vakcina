from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import class_mapper
from flask import Flask
from sqlalchemy.orm import class_mapper

app = Flask(__name__)
db = SQLAlchemy(app)


class DictMixin(object):
    def asdict(self):
        return dict((col.name, getattr(self, col.name))
                    for col in class_mapper(self.__class__).mapped_table.c)


class ClientLog(UserMixin, db.Model):
    __tablename__ = 'client_log'
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    first = db.Column(db.Boolean)


class Clients(db.Model, DictMixin):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, db.ForeignKey('client_log.id'), primary_key=True, nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    sex = db.Column(db.Integer, nullable=False)
    date_of_birth = db.Column(db.String(15), nullable=False)
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


class VaccControl(db.Model):
    __tablename__ = 'vacc_control'
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), primary_key=True, unique=False)
    vacc_id = db.Column(db.Integer, db.ForeignKey('vaccines.id'), primary_key=True, unique=False)
    date = db.Column(db.String(15), primary_key=True)

    def __repr__(self):
        return str({'client_id': self.client_id,
                    'vacc_id': self.vacc_id,
                    "date": self.date})


class DictMixin(object):
    def asdict(self):
        return dict((col.name, getattr(self, col.name))
                    for col in class_mapper(self.__class__).mapped_table.c)


# class Clients(db.Model, DictMixin):
#     __tablename__ = 'clients'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
#     email = db.Column(db.String(255), nullable=False)
#     first_name = db.Column(db.String(255), nullable=False)
#     last_name = db.Column(db.String(255), nullable=False)
#     sex = db.Column(db.Integer, nullable=False)
#     date_of_birth = db.Column(db.String(255), nullable=False)
#     location = db.Column(db.String(255), nullable=False)
#
#     def __repr__(self):
#         return str({'id': self.id,
#                     'authentification_key': self.authentification_key,
#                     'email': self.email,
#                     'first_name': self.first_name,
#                     'last_name': self.last_name,
#                     'sex': self.sex,
#                     'date_of_birth': self.date_of_birth,
#                     'location': self.location})


class Additional(db.Model, DictMixin):
    __tablename__ = 'additional'
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), primary_key=True)
    travels_per_year = db.Column(db.Integer, nullable=False)
    sick_per_year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return str({'client_id': self.client_id,
                    'travels_per_year': self.travels_per_year,
                    'sick_per_year': self.sick_per_year})


class AgeVaccination(db.Model, DictMixin):
    __tablename__ = "age_vaccination"
    vacc_id = db.Column(db.Integer, db.ForeignKey('vaccines.id'), primary_key=True)
    age = db.Column(db.Float, primary_key=True)

    def __repr__(self):
        return str({'vacc_id': self.vacc_id,
                    'age': self.age})


class Hospitals(db.Model, DictMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255))
    lon = db.Column(db.Float, nullable=False)
    lat = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return str({'id': self.id,
                    'name': self.name,
                    'address': self.address,
                    'lon': self.lon,
                    'lat': self.lat})


class PresenceIn(db.Model, DictMixin):
    hospital_id = db.Column(db.Integer, db.ForeignKey('hospitals.id'), primary_key=True)
    vacc_id = db.Column(db.Integer, db.ForeignKey('vaccines.id'), primary_key=True)
    num_present = db.Column(db.Integer)

    def __repr__(self):
        return str({'hospital_id': self.hospital_id,
                    'vacc_id': self.vacc_id,
                    'num_present': self.num_present})


# class Medicines(db.Model, DictMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), nullable=False)
#
#     def __repr__(self):
#         return str({'id': self.id,
#                     'name': self.name})
#
#
# class Allergies(db.Model, DictMixin):
#     client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), primary_key=True)
#     medicine_id = db.Column(db.Integer, db.ForeignKey('medicines.id'), primary_key=True)
#
#     def __repr__(self):
#         return str({'client_id': self.client_id,
#                     'medicine_id': self.medicine_id})
