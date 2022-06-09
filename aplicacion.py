#Se importa la biblioteca de Flask
from flask import Flask, redirect, render_template, request, url_for, flash

#Objeto para inicializar la aplicación
#1. Nombre por defecto
#2. Ruta donde están los templates
app = Flask(__name__, template_folder='templates')

#Seguridad de la app
app.secret_key = '0000'

#Almacenamiento de tareas
datos_formulario = []

#Primer controlador: inicial
#Lista actual de tareas pendientes y Formulario HTML para ingresar nuevas tareas
@app.route('/')
def principal():
    return render_template('principal.html', datos_formulario=datos_formulario)

#Ruta de página 1
@app.route('/drones')
def drones():
    return render_template('/drones.html')

#Ruta de página dron1
@app.route('/dron1')
def dron1():
    return render_template('/dron1.html')

#Ruta de página dron2
@app.route('/dron2')
def dron2():
    return render_template('/dron2.html')

#Ruta de página dron3
@app.route('/dron3')
def dron3():
    return render_template('/dron3.html')

#Ruta de página 2
@app.route('/aeromodelismo')
def aeromodelismo():
    return render_template('/aeromodelismo.html')

#Controlador para el envío de un nuevo elemento
@app.route('/enviar', methods=['POST'])
def enviar():
    if request.method == 'POST':
        
        #Campos a llenar
        nombres = request.form['nombres']
        celular = request.form['celular']
        correo_electronico = request.form['correo_electronico']

        #Validación para que los campos no sean nulos
        if nombres == '' or correo_electronico == '':
            flash('LLenar todos los campos')
            return redirect(url_for('principal'))
        
        else:
            flash('¡Tarea agregada exitosamente!')
            datos_formulario.append({'nombres': nombres, 'celular': celular, 'correo_electronico': correo_electronico})
            return redirect(url_for('principal'))

#Controlador: Limpiar formulario
@app.route('/borrar', methods=['POST'])
def borrar():
    if request.method == 'POST':
        
        #Verificación de datos
        if datos_formulario == []:
            flash('Formulario vacío')
            return redirect(url_for('principal'))

        else:
            datos_formulario.clear()
            flash('Formulario borrado')
            return redirect(url_for('principal'))

#Método para correr la aplicación
if __name__ == '__main__':
    app.run(debug=True)