## Build a simple flask web application
from flask import Flask,render_template
"""
It creates an instance of the Flask class,
Which will be your WSGI (Web Server Gateway Interface) application.
"""
app=Flask(__name__)

#Decorator
@app.route("/")
def welcome():
    return "Welcome to this best Flask course. This should be a amazing course"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)