# Assignment: Great Number Game
# Create a site that when a user loads it creates a random number between 1-100 and stores the number in session. Allow the user to guess at the number and tell them when they are too high or too low. If they guess the correct number tell them and offer to play again.

from flask import (Flask, render_template, request, redirect, session)
import random # import the random module



app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes

@app.route('/')

def greatnumbergame():
    session['someKey'] = random.randrange(0, 101) # random number between 0-100
    print session['someKey']
    # Remove something from session like so:
    # session.pop('someKey')
    return render_template('index.html')

@app.route('/number', methods=['POST'])
def number():
    session['number'] = request.form['number']
    if int(session['number']) == int(session['someKey']) :
        comment = int(session['someKey']), "was the number"
        play = "same"
    elif int(session['number'] ) < int(session['someKey']):
        comment = "Too low"
    elif int(session['number'] ) > int(session['someKey']):
        comment = "Too High"
    print session['number'] 
    return render_template('index.html',comment=comment,play=play) 
app.run(debug=True)