#from app import app
##Interacao para chamar html e manda o aqruivo para frente
#from flask import render_template


#@app.route('/')
#@app.route('/index')
#def index():
#    #return "Hello World"
#   return render_template("index.html", username="Ricardo")

from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Feulo'}
    #criar postes
    posts = [
        {'author': {'username': 'Maria'}, 'body': "Olá da Maria"},
        {'author': {'username': 'Feulo'}, 'body': "Olá!"}
    ]
    return render_template("index.html", user=user, posts=posts)