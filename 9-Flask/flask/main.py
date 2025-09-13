## Build a simple flask web application
from flask import Flask
"""
It creates an instance of the Flask class,
Which will be your WSGI (Web Server Gateway Interface) application.
"""
app=Flask(__name__)

#Decorator
@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"
@app.route("/index")
def index():
    return "Welcome to the index page"


if __name__=="__main__":
    app.run(debug=True)

