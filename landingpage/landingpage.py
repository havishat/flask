# Assignment: Landing Page
# Create a flask project capable of handling the following routes.

from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")  #This route should serve a view file called index.html and display a greeting. This will be considered our 'root route'.
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/ninjas')
def ninjas():
  return render_template("ninjas.html") 

@app.route('/dojo/news')
def dojonews():
    return render_template("dojo.html") 
    print "Got Post Info"
    # we'll talk about the following two lines after we learn a little more
    # about forms
    name = request.form['name']
    email = request.form['email']
    # redirects back to the '/' route
    return redirect('/')

app.run(debug=True) # run our server