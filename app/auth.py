from flask import redirect, url_for, session, flash, request
from functools import wraps


def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'usuario' not in session:
            rule = request.url_rule
            if str(rule).strip() != '/':
                mensaje = "Acceso restringido.. no estás logueado"
                flash(mensaje, 'danger')
            return redirect(url_for('login'))
        return func(*args, **kwargs)
    return decorated_function

def not_logged_in_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'usuario' in session:
            flash('Ya estás logueado..', 'info')
            return redirect(url_for('index'))
        return func(*args, **kwargs)
    return decorated_function
