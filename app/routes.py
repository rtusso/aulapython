from app import app
#Interacao para chamar html e manda o aqruivo para frente
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    #return "Hello World"
    return render_template("index.html")