from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from models import ClientLog, db


auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = ClientLog.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))
    login_user(user, remember=remember)
    print(user.first)
    if user.first == True:
        user.first = False
        db.session.commit()
        print(user.first)
        return redirect(url_for('main.profile'))
    return redirect(url_for('main.home'))


@auth.route('/signup')
def signup():
    return render_template('login.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    user = ClientLog.query.filter_by(
        email=email).first()
    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))
    db.session.add(
        ClientLog(name=name, email=email, password=generate_password_hash(password, method='sha256'), first=True))
    db.session.commit()
    print(ClientLog.query.all())
    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
