## Importamos flask
from flask import Flask, render_template, send_from_directory
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app)

## Definimos la ruta principal
@app.route("/")
def HolaFlask():
    return render_template("index.html")

## Programa para calcular el promedio de notas
@app.route("/notas")
@app.route("/notas/<float:nota1>/<float:nota2>/<float:nota3>")
def notas(nota1=0, nota2=0, nota3=0):
    resultado = (nota1*30)/100 + (nota2*30)/100 + (nota3*40)/100
    return f"<h1>El resultado es: {resultado}</h1> <hr>"


    ## Tomamos la tercera ruta y la reemplazamos por el siguiente ejemplo
## 2.) Un programa que al capturar la edad de una persona diga si es:
## Menor de edad (Menor a 18 años)
## Adulto (Mayor o igual a 18 años y menor a 60 años)
## Adulto mayor (Mayor o igual a 60 años)
@app.route("/edades")
@app.route("/edades/<int:edad>")
def edades(edad=0):
    if edad < 18:
        R = "menor de edad"
    elif edad < 60:
        R = "Adulto"
    else:
        R = "Adulto mayor"
    return f"<h1>La persona es: {R}</h1> <hr>"



## Creamos otra ruta ruta relizamos el siguiente ejemplo
## 3.) Programa que crea arreglos con valores aleatorios
## Importamos la libreria numpy si no existe la instalamos con: pip install numpy
import numpy as np
@app.route("/arreglos")
@app.route("/arreglos/<int:valores>/<int:columnas>")
@app.route("/arreglos/<int:valores>/<int:columnas>/<int:filas>")
def arreglos(valores=0,columnas=0,filas=0):
    if filas==0:
        arreglo=np.random.randint(valores, size=columnas)
    else:
        arreglo=np.random.randint(valores, size=(filas,columnas))

    return f"<h1>El arreglo aleatorio es: {arreglo}</h1> <hr>"

@app.route('/app.js')
def servir_js():
    return send_from_directory('.', 'app.js')

if __name__ == "__main__":
    app.run(debug=True)







