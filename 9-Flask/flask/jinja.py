## Build a simple flask web application
### Variable Rule
### Jinja 2 template engine

### Jinja2 Template Engine
"""
{{ }} expressions to print output in html
{{%...%}} condition, for loops
{#...#} this is for comment
"""
from flask import Flask,render_template,request,redirect,url_for
# """
# It creates an instance of the Flask class,
# Which will be your WSGI (Web Server Gateway Interface) application.
# """
app=Flask(__name__)

#Decorator
@app.route("/")
def welcome():
    return "Welcome to this best Flask course. This should be a amazing course"

@app.route("/index", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

# @app.route("/submit", methods=['GET','POST'])
# def submit():
#     if request.method=='POST':
#         name=request.form['name']
#         return f'Hello {name}!'
#     return render_template('form.html')

@app.route("/successres/<int:score>")
def successres(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"

    exp={'score':score, "res":res}
    return render_template('result1.html', results=exp)
    

@app.route("/successif/<int:score>")
def successif(score):
    return render_template('result.html', results=score)
    

@app.route("/fail/<int:score>")
def fail(score):
    return render_template('result.html', results=score)

@app.route('/submit', methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        datascience=float(request.form['datascience'])

        total_score=(science+maths+c+datascience)/4
        return redirect(url_for('successres', score=int(total_score)))
    return render_template("getresult.html")
if __name__=="__main__":
    app.run(debug=True)