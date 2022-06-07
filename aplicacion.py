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

#Ruta de página 2
@app.route('/aeromodelismo')
def aeromodelismo():
    return render_template('/aeromodelismo.html')

#Método para correr la aplicación
if __name__ == '__main__':
    app.run(debug=True)