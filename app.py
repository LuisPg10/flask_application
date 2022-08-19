from flask import Flask, render_template, request, flash
from settings.config import Configuration
from forms import UserRegister, UserSession
import database as db

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
    else:
        email = request.form["email"]
        name = request.form["name"]
        last_name = request.form["last_name"]
        password = request.form["password"]

        db.sql_add_user(email, name, last_name, password)
        return render_template("great_register.html", title = "Felicitaciones!")

@app.route("/sign_in", methods = ["GET", "POST"])
def session():

    list_data = db.sql_check_user()
    passed = False
    form = UserSession()
    email = request.form.get("email", False)
    password = request.form.get("password", False)

    for data in list_data:
        if data[0] == email and data[1] == password:
            passed = True

    if request.method == "GET":
        return render_template("session.html", form = form, title = "Inicia sesión")

    elif not passed:
        print("Usuario o contraseña incorrectos")
        return render_template("session.html", form = form, title = "Inicia sesión")

    elif request.method == "POST" and passed:
        return render_template("reservation.html", title = f"Bienvenido")

app.run(host = "localhost", port = 1024)