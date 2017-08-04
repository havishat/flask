# Assignment: Dojo Survey
# Build a flask application that accepts a form submission, redirects, and presents the submitted data on a results page.

from flask import Flask, render_template, request, redirect
app = Flask(__name__)
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
    return render_template('results.html', Name=name, Dojo_location=Dojo_location, Favorite_Language=Favorite_Language, Comment=Comment)

@app.route('/goback')
def goback():
  return redirect('/')

app.run(debug=True) # run our server