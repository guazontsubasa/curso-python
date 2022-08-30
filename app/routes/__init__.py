from flask import render_template, redirect, url_for, session, flash, request
from app.auth import login_required, not_logged_in_required
from app import app
from app.forms import LoginForm, IngresarPersonalForm
from app.handlers import eliminar_personal, get_personal_por_id, validar_usuario, get_personal, agregar_personal
from app.routes.personal import *


@app.route('/')  # http://localhost:5000/
@app.route('/index')
@login_required
def index():
    if request.method == 'GET' and request.args.get('borrar'):
        eliminar_personal(request.args.get('borrar'))
        flash('Se ha eliminado el empleado', 'success')
    return render_template('index.html', titulo="Inicio", personal=get_personal())




@app.route('/login', methods=['GET', 'POST'])
@not_logged_in_required
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        usuario = login_form.usuario.data
        password = login_form.password.data
        if validar_usuario(usuario, password):
            session['usuario'] = usuario
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('index'))
        else:
            flash('Credenciales inválidas', 'danger')
    return render_template('login.html', titulo="Login", login_form=login_form)


@app.route('/logout')
@login_required
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

