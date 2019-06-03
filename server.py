from flask import Flask, Blueprint, render_template, redirect

app = Flask(__name__)
app.url_map.strict_slashes = False

blueprint = Blueprint("", __name__)


@blueprint.route("/login")
def home():
    return render_template("login.html")


@blueprint.route("/profile")
def profile():
    return render_template("profile.html")


@blueprint.route("/home")
def home_registered():
    return render_template("home.html")


@blueprint.route("/search")
def home_map():
    return render_template("vaccine.html")


@blueprint.route("/history")
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


app.register_blueprint(blueprint, url_prefix="/")


if __name__ == '__main__':
    app.run(debug=True)
