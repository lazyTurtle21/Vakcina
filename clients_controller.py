from flask import Flask, jsonify, request, abort, Blueprint, make_response
from config import Config
from flask_sqlalchemy import SQLAlchemy
import models
from json import dumps

from models import db

# app_db = Bl
app_db = Blueprint('app_db', __name__)

# app_db.config.from_object(Config)
# db = SQLAlchemy(app_db)


@app_db.route('/clients', methods=['GET'])
def get_clients():
    clients = models.Clients.query.all()
    result = [client.asdict() for client in clients]
    return jsonify(result)


@app_db.route('/clients/<int:id>', methods=['GET'])
def get_client(id):
    client = models.Clients.query.filter_by(id=id).first()
    result = client.asdict()
    return jsonify(result)


@app_db.route('/clients/', methods=['POST'])
def add_client():
    cjson = request.get_json()
    if cjson.keys() != {"email", "first_name", "last_name", "sex", "date_of_birth",
                        "location"}:
        abort(422)
    elif None in (cjson["email"], cjson["first_name"], cjson["last_name"], cjson["sex"],
                  cjson["date_of_birth"], cjson["location"]):
        abort(422)

    elif len(cjson["email"]) > 255 or len(cjson["first_name"]) > 255 or len(cjson["last_name"]) > 255 or len(
            cjson["date_of_birth"]) > 255 or len(cjson["location"]) > 255:
        abort(422)

    client = models.Clients(email=cjson['email'], first_name=cjson['first_name'],
                          last_name=cjson['last_name'], sex=cjson['sex'],
                          date_of_birth=cjson['date_of_birth'], location=cjson['location'])
    db.session.add(client)
    db.session.commit()

    result = client.asdict()
    return jsonify(result)


@app_db.route('/vaccines', methods=['GET'])
def get_vaccines():
    vaccines = models.Vaccines.query.all()
    result = [vac.asdict() for vac in vaccines]
    return jsonify(result)


@app_db.route('/vaccines/<int:id>', methods=['GET'])
def get_vaccina(id):
    vaccina = models.Vaccines.query.get(id)
    result = vaccina.asdict()
    return jsonify(result)


@app_db.route('/vaccines/', methods=['POST'])
def add_vaccina():
    vaccina_json = request.get_json()
    vaccina = models.Vaccines(name=vaccina_json['name'])
    db.session.add(vaccina)
    db.session.commit()
    result = vaccina.asdict()
    return jsonify(result)


@app_db.route('/age_vaccination', methods=['GET'])
def get_age_vaccination():
    age_vaccina = models.AgeVaccination.query.all()
    result = [av.asdict() for av in age_vaccina]
    return jsonify(result)


@app_db.route('/age_vaccination/', methods=['POST'])
def add_age_vaccination():
    age_vaccination_json = request.get_json()
    age_vaccination = models.AgeVaccination(vacc_id=age_vaccination_json["vacc_id"], age=age_vaccination_json["age"])
    db.session.add(age_vaccination)
    db.session.commit()
    result = age_vaccination.asdict()
    return jsonify(result)


@app_db.route('/vacc_control/<int:client_id>', methods=['GET'])
def get_client_vacc_control(client_id):
    vacc_control = models.VaccControl.query.filter_by(client_id=client_id).all()
    result = [vacc.asdict() for vacc in vacc_control]
    for vac in result:
        del vac['client_id']
    return jsonify(result)


@app_db.route('/vacc_control/', methods=['POST'])
def add_vac_control():
    vac_control_json = request.get_json()
    vac_control = models.VaccControl(client_id=vac_control_json["client_id"], vacc_id=vac_control_json["vacc_id"],
                                   is_done=vac_control_json["is_done"])
    db.session.add(vac_control)
    db.session.commit()
    result = vac_control.asdict()
    return jsonify(result)


@app_db.route('/hospitals/', methods=['POST'])
def add_hospital():
    hospital_json = request.get_json()
    hospital = models.Hospitals(name=hospital_json['name'], address=hospital_json['address'],
                              lon=hospital_json['lon'], lat=hospital_json['lat'])
    db.session.add(hospital)
    db.session.commit()
    result = hospital.asdict()
    return jsonify(result)


@app_db.route('/hospitals/<string:vacc_name>', methods=['GET'])
def get_hospital_by_vacc(vacc_name):
    vacc_id = models.Vaccines.query.filter_by(name=vacc_name).first()
    if not vacc_id:
        return jsonify({})
    vacc_id = vacc_id.asdict()['id']
    hospitals_with_vac1 = models.PresenceIn.query.filter_by(vacc_id=vacc_id).all()
    hospitals_with_vac2 = [i.asdict() for i in hospitals_with_vac1]

    for hosp in hospitals_with_vac2:
        if hosp["num_present"] < 1:
            del hospitals_with_vac2[hospitals_with_vac2.index(hosp)]

    hospitals = []
    for h in hospitals_with_vac2:
        hospital = models.Hospitals.query.filter_by(id=h["hospital_id"]).first().asdict()
        hospital["num_present"] = h["num_present"]
        del hospital["id"]
        hospitals.append(hospital)

    return jsonify(hospitals)


@app_db.route('/presence_in/', methods=['POST'])
def add_presence_in():
    presence_in_json = request.get_json()
    presence_in = models.PresenceIn(hospital_id=presence_in_json['hospital_id'], vacc_id=presence_in_json['vacc_id'],
                                  num_present=presence_in_json['num_present'])
    db.session.add(presence_in)
    db.session.commit()
    result = presence_in.asdict()
    return jsonify(result)


if __name__ == "__main__":
    db.create_all()
    app_db.run(debug=True)
