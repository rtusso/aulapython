#from app import app
##Interacao para chamar html e manda o aqruivo para frente
#from flask import render_template


#@app.route('/')
#@app.route('/index')
#def index():
#    #return "Hello World"
#   return render_template("index.html", username="Ricardo")

from app import app
from flask import render_template, request


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Feulo'}
    posts = [
        {'author': {'username': 'Maria'}, 'body': "Olá da Maria"},
        {'author': {'username': 'Mario'}, 'body': "Olá!"}
    ]
    return render_template("index.html", user=user, posts=posts)

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        print(request.values.get("user"), request.values.get("pass"), request.values.get("remember"))
    return render_template("login.html" , title="Login")