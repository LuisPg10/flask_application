from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, EmailField
from wtforms.validators import DataRequired, EqualTo

class BaseForm(FlaskForm):
    email = EmailField("Email",
        validators = [DataRequired()],
        render_kw = {"placeholder": "Email"}
    )
    password = PasswordField("Contraseña",
        validators = [DataRequired(),
        EqualTo("confirm", message = "Las contraseñas deben coincidir")],
        render_kw = {"placeholder": "Contraseña"}
    )

class UserRegister(BaseForm):
    name = StringField("Nombre",
        validators = [DataRequired()],
        render_kw = {"placeholder": "Nombre"})
    
    last_name = StringField("Apellido",
        validators = [DataRequired()], 
        render_kw = {"placeholder": "Apellido"})

    confirm = PasswordField("Confirmar contraseña",
        validators = [DataRequired()],
        render_kw = {"placeholder": "Confirmar contraseña"}
    )

    terms = BooleanField("Acepto los terminos y condiciones", validators = [DataRequired()])
    register = SubmitField("Registrar", validators = [DataRequired()])

class UserSession(BaseForm):
    remember = BooleanField("Recordar", validators = [DataRequired()])

