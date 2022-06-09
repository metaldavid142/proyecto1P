#Se importa la biblioteca de Flask
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def principal():
    return render_template('principal.html')

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

#Método para correr la aplicación
if __name__ == '__main__':
    app.run(debug=True)