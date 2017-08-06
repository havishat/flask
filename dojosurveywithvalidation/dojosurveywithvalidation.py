# Assignment: Dojo Survey
# Build a flask application that accepts a form submission, redirects, and presents the submitted data on a results page.

from flask import Flask, render_template, session, request, redirect, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
#index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/results', methods=['POST']) 
def create_user():
    print "Got Post Info"
    name = request.form['name']
    Dojo_location = request.form['Dojo Location']
    Favorite_Language = request.form['Favorite Language']
    Comment = request.form['Comment']
    # redirects back to the '/' route
    #return redirect('/')
    if len(name) == 0  or len(Comment) == 0:
      flash("Cannot be empty!") # just pass a string to the flash function
      return render_template('index.html')
    elif len(Comment) > 120 : 
      flash("Comments is more than 120 characters. Please type less than 120 characters")
      return render_template('index.html')
    return render_template('results.html', Name=name, Dojo_location=Dojo_location, Favorite_Language=Favorite_Language, Comment=Comment)

@app.route('/goback')
def goback():
  return redirect('/')

app.run(debug=True) # run our server