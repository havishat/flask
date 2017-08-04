# Assignment: Great Number Game
# Create a site that when a user loads it creates a random number between 1-100 and stores the number in session. Allow the user to guess at the number and tell them when they are too high or too low. If they guess the correct number tell them and offer to play again.

from flask import (Flask, render_template, request, redirect, session)
import random # import the random module



app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes

@app.route('/')

def greatnumbergame():
    random.randrange(0, 101) # random number between 0-100
    # Set session like so:
    # session['someKey'] = 50
    # Remove something from session like so:
    # session.pop('someKey')
@app.route('/number', methods=['POST'])
def create_user():
    number = request.form['number']
    return redirect('/') # redirects back to the '/' route
app.run(debug=True)