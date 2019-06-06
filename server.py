import os
from flask import Blueprint, render_template, redirect, url_for, request, flash,jsonify
from flask_login import login_required, current_user
from flask_login import LoginManager
from clients_controller import app_db
from models import Clients, ClientLog, app, db, VaccControl, Vaccines
import datetime
from models import Hospitals, AgeVaccination, VaccControl, PresenceIn

main = Blueprint('main', __name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'

# host = os.environ.get('DB_HOST', 'localhost')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{user}:{password}@{host}/{database}'.format(
#     user='client', password='Password-1234', database='vakcina', host=host)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///vaccina.db'

app.config['JSON_AS_ASCII'] = False



app.register_blueprint(app_db)

db.init_app(app)
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = "Щоб продовжити роботу необхідно увійти"
login_manager.init_app(app)
app.url_map.strict_slashes = False

blueprint = Blueprint("", __name__)


@main.route("/")
@login_required
def index():
    return redirect(url_for('main.home'))


@main.route("/home")
@login_required
def home():
    return render_template('home.html')


@login_required
@blueprint.route("/current_user")
def get_current_user():
    return jsonify({"id": current_user.id})


@main.route('/profile')
@login_required
def profile():
    cli = Clients.query.filter_by(id=current_user.id).first()
    return render_template('profile.html', client=cli, vaccs=[l.name for l in
                                                              db.session.query(Vaccines).join(VaccControl).filter_by(
                                                                  client_id=current_user.id).all()])


@main.route('/profile', methods=['POST'])
def get_profile():
    cli = Clients.query.filter_by(id=current_user.id).first()

    if cli is None:
        cli = Clients(id=current_user.id, first_name=request.form.get('firstname'),
                      last_name=request.form.get('lastname'),
                      sex=request.form.get('sex'),
                      date_of_birth=request.form.get('date'), location=request.form.get('location'))
        db.session.add(cli)

        for i in range(1, 11):
            if request.form.get('v{}'.format(i)) is not None:
                # v = Vaccines(name=request.form.get('v{}'.format(i)))
                # db.session.add(v)

                vacc = VaccControl(client_id=current_user.id,
                                   vacc_id=Vaccines.query.filter_by(name=request.form.get('v{}'.format(i))).first().id,
                                   date=datetime.date.today().isoformat())
                db.session.add(vacc)

    else:
        cli.first_name = request.form.get('firstname')
        cli.last_name = request.form.get('lastname')
        cli.sex = request.form.get('sex')
        cli.date_of_birth = request.form.get('date')
        cli.location = request.form.get('location')
        # for i in range(1, 11):
        #     if request.form.get('v{}'.format(i)) is not None:
        #         VaccControl.query.filter_by().delete()
    db.session.commit()

    if request.form.get('firstname') == '' or request.form.get('lastname') == '' or request.form.get(
            'date') == '' or request.form.get('location') == '':
        flash("*")
        return redirect(url_for('main.profile'))
    return redirect(url_for('main.home'))


@blueprint.route("/search")
@login_required
def home_map():
    return render_template("vaccine.html")


@blueprint.route("/history")
@login_required
def history():
    return render_template("history.html")


@blueprint.route("/epidemics")
def epidemics():
    return render_template("epidemics.html")


@blueprint.route("/about")
def about():
    return render_template("about.html")


@blueprint.route("/news")
def news():
    return render_template("news.html")


@blueprint.route("/travel")
def travel():
    return render_template("travel.html")


# app.route("/")(lambda: redirect("/vakcina"))
@login_manager.user_loader
def load_user(user_id):
    return ClientLog.query.get(int(user_id))


from auth import auth as auth_blueprint

app.register_blueprint(auth_blueprint)
app.register_blueprint(main)
app.register_blueprint(blueprint, url_prefix="/")

def load_csv_age_vaccines():
    with open(r'data/vacc_age.csv') as f:
        line, lines = f.readline(), f.readlines()

    for line in lines:
        id, age = line.strip().split(sep=';')
        db.session.add(AgeVaccination(vacc_id=int(id), age=float(age)))

    db.session.commit()


def load_csv_vaccines():
    with open('data/vaccines.csv') as f:
        line, lines = f.readline(), f.readlines()

    for line in lines:
        id, name = line.strip().split(sep=';')
        db.session.add(Vaccines(vacc_id=int(id), name=name))

    db.session.commit()


def load_csv_hospitals():
    with open('./data/hospitals.csv', encoding="utf-8") as f:
        line, lines = f.readline(), f.readlines()

    for line in lines:
        id, name, address, longitude, latitude = line.strip().split(sep=';')
        db.session.add(Hospitals(id=int(id), name=name, address=address, lon=longitude, lat=latitude))

    db.session.commit()


def load_csv_presence_in():
    with open('./data/presence_in.csv') as f:
        line, lines = f.readline(), f.readlines()

    for line in lines:
        hospital_id, vacc_id, num_present = line.strip().split(sep=';')
        print(hospital_id)
        db.session.add(PresenceIn(hospital_id=int(hospital_id), vacc_id=int(vacc_id), num_present=int(num_present)))

    db.session.commit()



if __name__ == '__main__':
    db.create_all()
    # load_csv_age_vaccines()
    # load_csv_hospitals()
    # load_csv_presence_in()
    # load_csv_age_vaccines()

    app.run(debug=True, port=4000)
