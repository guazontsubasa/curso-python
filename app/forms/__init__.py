from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, IntegerField
from wtforms.validators import DataRequired, Length
import datetime


class LoginForm(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired('Este campo es requerido')])
    password = PasswordField('Contraseña', validators=[DataRequired('Este campo es requerido')])
    enviar = SubmitField('Iniciar sesión')


class IngresarPersonalForm(FlaskForm):
    fecha = DateField('Fecha', default=datetime.datetime.now, validators=[DataRequired('El campo Nombre es requerido')])
    nombre = StringField('Nombre', validators=[Length(max=50)])
    apellido = StringField('Apellido', validators=[Length(max=50)])
    dni = IntegerField('DNI', validators=[DataRequired('El campo Nombre es requerido')])
    motivo = StringField('Motivo', validators=[DataRequired('El campo Nombre es requerido')])
    enviar = SubmitField('Guardar entrada')
    cancelar = SubmitField('Cancelar', render_kw={'class': 'btn btn-danger', 'formnovalidate': 'True'})