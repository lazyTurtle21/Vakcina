# import os
from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from flask_login import login_required, current_user
from flask_login import LoginManager
from clients_controller import app_db
from models import Clients, ClientLog, app, db, VaccControl, Vaccines
import datetime
from random import randint

main = Blueprint('main', __name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'

# host = os.environ.get('DB_HOST', 'localhost')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{user}:{password}@{host}/{database}'.format(
#     user='client', password='Password-1234', database='vakcina', host=host)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vaccina.db'

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
    print(VaccControl.query.all())
    print(current_user.id)
    return render_template('profile.html', client=cli, vaccs=[l.name for l in
                                                              db.session.query(Vaccines).join(VaccControl).filter_by(
                                                                  client_id=current_user.id).filter_by(
                                                                  is_done=True).all()])


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
            # if request.form.get('v{}'.format(i)) is not None:
            #     v = Vaccines(name=request.form.get('v{}'.format(i)))
            #     db.session.add(v)
            vacc = VaccControl(client_id=current_user.id,
                               vacc_id=Vaccines.query.filter_by(id=i).first().id,
                               date=(datetime.date.today() - datetime.timedelta(
                                   days=(730 - randint(1, 730)))).isoformat(),
                               is_done=True if request.form.get('v{}'.format(i)) is not None else False)

            db.session.add(vacc)

    else:
        cli.first_name = request.form.get('firstname')
        cli.last_name = request.form.get('lastname')
        cli.sex = request.form.get('sex')
        cli.date_of_birth = request.form.get('date')
        cli.location = request.form.get('location')
        for i in range(1, 11):
            if request.form.get('v{}'.format(i)) is None:
                temp = db.session.query(VaccControl).filter_by(client_id=current_user.id).filter_by(is_done=True).join(
                    Vaccines).filter_by(id=i).first()
                if temp is not None:
                    temp.is_done = False
            else:
                temp = db.session.query(VaccControl).filter_by(client_id=current_user.id).join(
                    Vaccines).filter_by(id=i).first()
                if temp is not None:
                    temp.is_done = True
                else:
                    db.session.add(VaccControl(client_id=current_user.id,
                                               vacc_id=Vaccines.query.filter_by(
                                                   name=request.form.get('v{}'.format(i))).first().id,
                                               date=datetime.date.today().isoformat(), is_done=True))

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

if __name__ == '__main__':
    db.create_all()
    print(VaccControl.query.all())
    app.run(debug=True, port=4000)
