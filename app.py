from flask import Flask, render_template, request
from settings.config import Configuration
from forms import UserRegister, UserSession

app = Flask(__name__)
app.config.from_object(Configuration)

@app.route("/")
def index():
    return render_template("index.html", title = "Hotel Baiyoke Tower")

@app.route("/sign_up", methods = ["GET", "POST"])
def register():
    if request.method == "GET":
        form = UserRegister()
        return render_template("register.html", form = form, title = "Nuevo usuario")
    elif request.method == "POST":
        return render_template("great_register.html", title = "Felicitaciones!")

@app.route("/sign_in")
def session():
    form = UserSession()
    return render_template("session.html", form = form, title = "Inicia sesión")

app.run(host = "localhost", port = 5000, debug = True)