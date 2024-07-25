from flask import Flask, render_template

app = Flask(__name__)

"""client - web browser sends requests e.g www.facebook.com DNS 
# 182.5.8.1:8000
server - listens for requests and sends response"""
#route /message

@app.route("/")
def index():
    return "Hello World!"


@app.route("/<name>")
def greet(name):
    return f"Good day {name}!"


@app.route("/users/<string:name>")  #www.vero456.com/users/<int: 1>
def hello(name):
      surname = "Osaghae"
      courses = "Calculus", "Mathematics" , "Physics" , "Robotics"
      return render_template("greeting.html", name=name, surname=surname , courses=courses)

@app.errorhandler(404)
def error_code(e):
     return render_template("404.html"), 404
