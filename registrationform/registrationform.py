from flask import Flask, render_template, session, request, redirect, flash
import re
import time
# from datetime import date 
# today = date.today()

name = re.compile(r'^[^0-9]+$')
EMAILisnotvalid = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
passd = re.compile(r'^([^0-9]*|[^A-Z]*)$')

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
#index route will handle rendering our form
@app.route('/')
def index(): 
  return render_template("index.html")

@app.route('/results', methods=['POST']) 
def form():
    email = request.form['email']
    First_name = request.form['First_name']
    Last_name = request.form['Last_name']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    Birthday = request.form['bday']
    # day = datetime.strptime(Birthday, '%d/%m/%Y')
    if len(First_name) == 0 or len(Last_name)== 0 or len(email)== 0 or len(password)== 0 or len(confirm_password)== 0 : 
      flash("Cannot be blank!")
      return render_template('index.html')
    elif not name.match(Last_name) or not name.match(First_name):
      flash("Cannot have number")
      return render_template('index.html')
    elif not EMAILisnotvalid.match(request.form['email']):
      flash("Invalid Email Address!")
      return render_template('index.html')
    elif len(password) < 8 :
      flash("Password should be more than 8 characters")
      return render_template('index.html')
    elif passd.match(request.form['password']):
      flash("least 1 uppercase letter and 1 numeric value")
      return render_template('index.html')
    elif password != confirm_password:
      flash("Password and Password Confirmation are not same")
      return render_template('index.html')
    # elif Birthday < today:
    #   flash("Please enter in the past ")
    else:
      flash("Thanks for submitting your information.")
    return render_template('results.html', email=email, First_name=First_name, Last_name=Last_name,password=password,confirm_password=confirm_password,Birthday=Birthday)

@app.route('/goback')
def goback():
  return redirect('/')


app.run(debug=True) # run our server
