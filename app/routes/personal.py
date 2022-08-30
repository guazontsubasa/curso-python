from flask import render_template, redirect, url_for, flash
from app.auth import login_required
from app import app
from app.forms import IngresarPersonalForm
from app.handlers import eliminar_personal, get_personal_por_id, agregar_personal



@app.route('/ingresar-personal', methods=['GET', 'POST'])
@login_required
def ingresar_personal():
    personal_form = IngresarPersonalForm()
    if personal_form.cancelar.data:  # si se apretó el boton cancelar, personal_form.cancelar.data será True
        return redirect(url_for('index'))
    if personal_form.validate_on_submit():
        datos_nuevos = { 
                        'fecha': personal_form.fecha.data.strftime('%d-%m-%Y'), 
                        'nombre': personal_form.nombre.data, 
                        'apellido': personal_form.apellido.data, 
                        'dni': personal_form.dni.data, 
                        'motivo': personal_form.motivo.data 
                        }
        agregar_personal(datos_nuevos)
        flash('Se ha agregado un nuevo empleado', 'success')
        return redirect(url_for('index'))
    return render_template('ingresar_personal.html', titulo="Personal", personal_form=personal_form)


@app.route('/editar-personal/<int:empleado>', methods=['GET', 'POST'])
@login_required
def editar_personal(empleado):
    personal_form = IngresarPersonalForm(data=get_personal_por_id(empleado))
    if personal_form.cancelar.data:  # si se apretó el boton cancelar, personal_form.cancelar.data será True
        return redirect(url_for('index'))
    if personal_form.validate_on_submit():
        datos_nuevos = { 
                        'fecha': personal_form.fecha.data.strftime('%d-%m-%Y'), 
                        'nombre': personal_form.nombre.data, 
                        'apellido': personal_form.apellido.data, 
                        'dni': personal_form.dni.data, 
                        'motivo': personal_form.motivo.data 
                        }
        eliminar_personal(empleado)  # Eliminamos el empleado antiguo
        agregar_personal(datos_nuevos)  # Agregamos el nuevo empleado
        flash('Se ha editado el empleado exitosamente', 'success')
        return redirect(url_for('index'))
    return render_template('editar_personal.html', titulo="Personal", personal_form=personal_form)

@app.route('/borrar-personal/<int:empleado>', methods=['GET'])
@login_required
def borrar_personal(empleado):
    eliminar_personal(empleado)
    flash('Se ha eliminado el empleado', 'success')
    return redirect(url_for('index'))