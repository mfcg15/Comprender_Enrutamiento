from cgitb import html
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return '¡Hola Mundo!'

@app.route('/dojo')
def dojo():
  return "¡Dojo!"

@app.route('/say/<string:name>')
def say(name):
  return "¡Hola, "+name.capitalize()+"!"

@app.route('/repeat/<int:cantidad>/<string:palabra>')
def repeat(cantidad,palabra):
    html = ""
    for i in range(0,cantidad):
        html += "<p>"+palabra+"</p>"
    return html

@app.errorhandler(404)
def error(err):
    return "¡Lo siento! No hay respuesta. Inténtalo otra vez"

if __name__=="__main__":
    app.run(debug=True)